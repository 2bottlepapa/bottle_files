#!/usr/bin/env python3
"""
小红书记忆导出工具 — 将笔记数据转为分类 Markdown 知识库

用法：
    python export_memory.py --input notes.json --output ~/xhs-memory/ --type favorites

输入 JSON 格式：
[
  {
    "title": "笔记标题",
    "content": "笔记正文",
    "author": "作者昵称",
    "feed_id": "帖子ID",
    "url": "https://www.xiaohongshu.com/explore/xxx",
    "likes": 1234,
    "favorites": 567,
    "comments": 89,
    "shares": 12,
    "images": ["url1", "url2"],
    "tags": ["美食", "烘焙"],
    "publish_time": "2024-01-15"
  }
]
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


# 标签到分类的映射（可扩展）
CATEGORY_MAP = {
    "美食": "🍜 美食",
    "烘焙": "🍜 美食",
    "做饭": "🍜 美食",
    "食谱": "🍜 美食",
    "下厨": "🍜 美食",
    "旅行": "✈️ 旅行",
    "旅游": "✈️ 旅行",
    "攻略": "✈️ 旅行",
    "景点": "✈️ 旅行",
    "酒店": "✈️ 旅行",
    "穿搭": "👗 穿搭",
    "时尚": "👗 穿搭",
    "outfit": "👗 穿搭",
    "护肤": "💄 美妆护肤",
    "美妆": "💄 美妆护肤",
    "化妆": "💄 美妆护肤",
    "健身": "💪 健身运动",
    "运动": "💪 健身运动",
    "减脂": "💪 健身运动",
    "瑜伽": "💪 健身运动",
    "读书": "📚 读书学习",
    "学习": "📚 读书学习",
    "考研": "📚 读书学习",
    "英语": "📚 读书学习",
    "编程": "💻 科技",
    "AI": "💻 科技",
    "数码": "💻 科技",
    "收纳": "🏠 家居生活",
    "装修": "🏠 家居生活",
    "家居": "🏠 家居生活",
    "租房": "🏠 家居生活",
    "育儿": "👶 育儿",
    "宝宝": "👶 育儿",
    "萌宠": "🐾 宠物",
    "猫": "🐾 宠物",
    "狗": "🐾 宠物",
    "摄影": "📷 摄影",
    "拍照": "📷 摄影",
    "职场": "💼 职场",
    "面试": "💼 职场",
    "工作": "💼 职场",
}

DEFAULT_CATEGORY = "📂 未分类"


def classify_note(note: dict) -> str:
    """根据标签和内容推断笔记分类"""
    tags = note.get("tags", [])
    title = note.get("title", "")
    content = note.get("content", "")
    text = " ".join(tags) + " " + title + " " + content[:200]
    text_lower = text.lower()

    for keyword, category in CATEGORY_MAP.items():
        if keyword.lower() in text_lower:
            return category

    return DEFAULT_CATEGORY


def sanitize_filename(name: str) -> str:
    """清理文件名，移除不安全字符"""
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = name.strip(". ")
    if not name:
        name = "untitled"
    return name[:80]


def format_count(n) -> str:
    """格式化数字为可读形式"""
    if n is None:
        return "0"
    n = int(n)
    if n >= 10000:
        return f"{n / 10000:.1f}w"
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def generate_note_md(note: dict) -> str:
    """将单篇笔记转为 Markdown"""
    # 兼容 xhs-mcp 和 XHS-Downloader 两种不同的返回格式
    title = note.get("title", note.get("作品标题", "无标题"))
    author = note.get("author", note.get("作者昵称", "未知"))
    url = note.get("url", note.get("作品链接", ""))
    content = note.get("content", note.get("作品描述", ""))
    
    # 互动数据
    likes = note.get("likes", note.get("点赞数量", 0))
    favorites = note.get("favorites", note.get("收藏数量", 0))
    comments = note.get("comments", note.get("评论数量", 0))
    
    # 图片/标签/时间
    images = note.get("images", note.get("下载地址", []))
    if isinstance(images, str):
        images = images.split()
        
    tags = note.get("tags", note.get("作品标签", ""))
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.replace("，", ",").split(",") if t.strip()]
        
    publish_time = note.get("publish_time", note.get("发布时间", ""))

    tags_str = ", ".join(f'"{t}"' for t in tags) if tags else ""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        "---",
        f'title: "{title}"',
        f'author: "{author}"',
        f'url: "{url}"',
        f"likes: {likes}",
        f"favorites: {favorites}",
        f"comments: {comments}",
        f"tags: [{tags_str}]",
        f'exported_at: "{now}"',
        "---",
        "",
        f"# {title}",
        "",
        f"> 作者：{author}",
    ]

    if publish_time:
        lines.append(f"> 发布时间：{publish_time}")
    if url:
        lines.append(f"> 原文：{url}")

    lines.extend(["", "---", "", content, ""])

    if images:
        lines.append("## 图片")
        lines.append("")
        for i, img_url in enumerate(images, 1):
            lines.append(f"![图片{i}]({img_url})")
            lines.append("")

    lines.extend([
        "## 互动数据",
        "",
        f"👍 {format_count(likes)} 点赞 · "
        f"⭐ {format_count(favorites)} 收藏 · "
        f"💬 {format_count(comments)} 评论",
        "",
    ])

    return "\n".join(lines)


def generate_readme(
    categories: dict,
    note_type: str,
    total_count: int,
    output_dir: str,
) -> str:
    """生成 README.md 索引"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    type_label = "收藏" if note_type == "favorites" else "点赞"

    lines = [
        "# 📕 小红书记忆库",
        "",
        f"> 导出时间：{now}",
        f"> 总计：{total_count} 篇笔记",
        "",
        "---",
        "",
        f"## 📁 {type_label}笔记 ({total_count} 篇)",
        "",
    ]

    for category, notes in sorted(categories.items()):
        lines.append(f"### {category} ({len(notes)} 篇)")
        lines.append("")
        for note in notes:
            title = note.get("title", "无标题")
            safe_title = sanitize_filename(title)
            safe_cat = sanitize_filename(category)
            rel_path = f"{note_type}/{safe_cat}/{safe_title}.md"
            fav_count = format_count(note.get("favorites", 0))
            lines.append(f"- [{title}]({rel_path}) — ⭐ {fav_count} 收藏")
        lines.append("")

    return "\n".join(lines)


def export(input_path: str, output_dir: str, note_type: str):
    """主导出函数"""
    # 读取输入
    with open(input_path, "r", encoding="utf-8") as f:
        notes = json.load(f)

    if not isinstance(notes, list):
        print(f"ERROR: 输入文件格式错误，期望 JSON 数组", file=sys.stderr)
        sys.exit(1)

    print(f"📖 读取 {len(notes)} 篇笔记")

    # 分类
    categories = defaultdict(list)
    for note in notes:
        category = classify_note(note)
        categories[category].append(note)

    print(f"📂 分为 {len(categories)} 个分类：{', '.join(categories.keys())}")

    # 创建目录并写入文件
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    written = 0
    for category, cat_notes in categories.items():
        safe_cat = sanitize_filename(category)
        cat_dir = output_path / note_type / safe_cat
        cat_dir.mkdir(parents=True, exist_ok=True)

        for note in cat_notes:
            title = note.get("title", "无标题")
            safe_title = sanitize_filename(title)
            filepath = cat_dir / f"{safe_title}.md"

            md_content = generate_note_md(note)
            filepath.write_text(md_content, encoding="utf-8")
            written += 1

    # 生成 README
    readme_content = generate_readme(categories, note_type, len(notes), output_dir)
    readme_path = output_path / "README.md"

    # 如果 README 已存在，追加内容
    if readme_path.exists():
        existing = readme_path.read_text(encoding="utf-8")
        readme_content = existing + "\n\n---\n\n" + readme_content

    readme_path.write_text(readme_content, encoding="utf-8")

    print(f"✅ 成功导出 {written} 篇笔记到 {output_path}")
    print(f"📋 索引文件: {readme_path}")
    print(f"SUCCESS")


def main():
    parser = argparse.ArgumentParser(description="小红书记忆导出 — JSON 转 Markdown 知识库")
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="输入 JSON 文件路径",
    )
    parser.add_argument(
        "--output", "-o",
        default=os.path.expanduser("~/xhs-memory"),
        help="输出目录路径 (默认: ~/xhs-memory)",
    )
    parser.add_argument(
        "--type", "-t",
        choices=["favorites", "likes"],
        default="favorites",
        help="导出类型: favorites (收藏) 或 likes (点赞)",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"ERROR: 输入文件不存在: {args.input}", file=sys.stderr)
        sys.exit(1)

    export(args.input, args.output, args.type)


if __name__ == "__main__":
    main()
