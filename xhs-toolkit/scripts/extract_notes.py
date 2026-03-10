#!/usr/bin/env python3
"""
小红书笔记批量提取工具 (XHS Bulk Extractor)

此工具直接调用 XHS-Downloader 源码批量提取笔记的高质量详情。
特别优化了沙箱环境下的路径限制问题，确保 Agent 调用不报错。

依赖：
- XHS-Downloader 源文件路径
- 已安装 XHS-Downloader 的 Python venv

用法：
    # 假设有个 notes_urls.txt 每行一个链接
    python extract_notes.py --input notes_urls.txt --output /tmp/extracted.json
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

# ========================================================
# 核心防御：沙箱路径屏蔽 (Monkey-Patching)
# ========================================================
# 很多系统 Agent 环境 (如 macOS Sandbox) 禁止直接在 Home 目录下创建不规范文件夹。
# XHS-Downloader 默认使用硬编码的相对路径创建 Volume 目录，会导致 PermissionError。
# 我们必须在导入 XHS 核心模块之前，篡改它的配置路径。

def apply_sandbox_patches(xhs_path: str):
    """注入补丁以绕过不安全的文件物理写入"""
    sys.path.append(xhs_path)
    
    try:
        # 1. 强制修改全局静态存储路径到 /tmp
        import source.module.static as xhs_static
        xhs_static.ROOT = Path("/tmp/XHS-Volume")
        xhs_static.ROOT.mkdir(exist_ok=True, parents=True)
        
        # 2. 拦截目录创建操作
        from source.module.manager import Manager
        Manager.create_folder = lambda self: None
        
        # 3. 拦截 SQLite 记录行为（防止由于数据库路径导致崩溃）
        from source.module.recorder import IDRecorder, DataRecorder, MapRecorder
        
        async def async_no_op(*args, **kwargs):
            return None

        async def async_return_self(self):
            return self

        # 屏蔽所有 SQLite 连接和上下文协议
        for RecorderClass in [IDRecorder, DataRecorder, MapRecorder]:
            RecorderClass._connect_database = async_no_op
            RecorderClass.__aenter__ = async_return_self
            RecorderClass.__aexit__ = async_no_op
            
        print("🔧 沙箱兼容补丁注入成功 (I/O 重定向至 /tmp)")
    except Exception as e:
        print(f"⚠️ 警告：沙箱补丁注入失败，如果遇到权限错误请检查 ({e})")

# ========================================================

async def extract_bulk(urls: list, xhs_path: str) -> list:
    """批量提取笔记详细信息"""
    apply_sandbox_patches(xhs_path)
    
    from source.application.app import XHS
    
    results = []
    
    # 实例化 XHS 下载器 (禁用所有强制物理保存机制)
    async with XHS(
        work_path="/tmp",
        folder_name="XHS-Temp",
        name_format="作品标题 作品描述",
        record_data=False,
        download_record=False,
        image_download=False,
        video_download=False
    ) as xhs:
        
        for i, url in enumerate(urls):
            print(f"[{i+1}/{len(urls)}] 正在获取: {url.split('?')[0]}")
            try:
                # 调用底层 extract 接口，download=False 返回全量 JSON 数据字典
                data = await xhs.extract(url, download=False)
                if data and isinstance(data, list) and len(data) > 0:
                    results.extend(data)
                    print(f"  👉 成功提取:《{data[0].get('作品标题', '无标题')[:20]}》")
                else:
                    print(f"  ❌ 未返回有效数据 (可能是 Cookie 失效或链接错误)")
            except Exception as e:
                print(f"  ❌ 提取过程中发生错误: {e}")
            
            # 反爬保护，严格遵从 1-2 秒延迟
            await asyncio.sleep(1.5)
            
    return results

def load_urls(input_path: str) -> list:
    """从纯文件、JSON或其他格式读取 URLs"""
    urls = []
    if not os.path.isfile(input_path):
        return urls
        
    try:
        # 假设是 JSON 数组结构 [{"url": "xxx"}, ...]
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and "url" in item:
                        urls.append(item["url"])
                    elif isinstance(item, str) and item.startswith("http"):
                        urls.append(item)
    except json.JSONDecodeError:
        # 纯文本读取
        with open(input_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("http"):
                    urls.append(line)
    return urls

def main():
    parser = argparse.ArgumentParser(description="小红书高吞吐笔记信息提取器")
    parser.add_argument("--input", "-i", required=True, help="包含笔记 URL 列表的文件路径")
    parser.add_argument("--output", "-o", default="/tmp/xhs_extracted.json", help="输出完整 JSON 数据的文件路径")
    parser.add_argument("--xhs-path", "-x", default=os.path.expanduser("~/ani/tools/XHS-Downloader"), help="XHS-Downloader 库的源码绝对路径")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.xhs_path):
        print(f"错误: 找不到 XHS-Downloader 源码路径 {args.xhs_path}", file=sys.stderr)
        print("请提供准确路径或克隆 JoeanAmier/XHS-Downloader 仓库", file=sys.stderr)
        sys.exit(1)
        
    urls = load_urls(args.input)
    if not urls:
        print(f"错误: 无法从 {args.input} 提取任何链接", file=sys.stderr)
        sys.exit(1)
        
    print(f"🚀 开始批量处理 {len(urls)} 条笔记链接...")
    
    try:
        if sys.version_info >= (3, 7):
            result = asyncio.run(extract_bulk(urls, args.xhs_path))
        else:
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(extract_bulk(urls, args.xhs_path))
            
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            
        print(f"✅ 任务完成！共成功提取 {len(result)} 条笔记数据。保存至 {args.output}")
        
    except KeyboardInterrupt:
        print("\n🛑 被用户强制中断")
        sys.exit(0)

if __name__ == "__main__":
    main()
