# notes — 笔记与素材

平铺放**单篇知识笔记**（`*.md` / `*.html`）；成套的集合保留自己的目录。

## 单篇笔记

按主题分组，一篇一行。原文全文和整理笔记放在一起，在"主题"列标明是原文还是笔记。

| 分类 | 回答的问题 | 篇数 |
|---|---|---|
| [Agent 与模型演进](#agent-与模型演进) | AI 模型和 Agent 往哪个方向走 | 2 |
| [AI 使用方法与思维](#ai-使用方法与思维) | 个人怎么把 AI 用好 | 1 |
| [产品经理与 AI 工具](#产品经理与-ai-工具) | PM 工作中用什么 AI 工具 | 1 |
| [组织与管理](#组织与管理) | 组织怎么适应 AI | 1 |
| [心态与成长](#心态与成长) | 与 AI 无关的个人成长 | 1 |

### Agent 与模型演进

| 文件 | 主题 | 来源 | 日期 |
|---|---|---|---|
| [林俊旸-推理模型的时代快结束了-原文.md](林俊旸-推理模型的时代快结束了-原文.md) | 原文全文：从推理思考到智能体思考，Agent RL 的基础设施挑战 | [x.com/AlchainHust](https://x.com/AlchainHust/status/2037183105602109498) · 留档 `bottleX/url-to-md/x.com/lin-junyang-article.md` | 2026-03-27 |
| [林俊旸-从推理到智能体思考-读书笔记.md](林俊旸-从推理到智能体思考-读书笔记.md) | 读书笔记：上一行原文的提炼；另有结构化笔记在 `bottleX/cc_notes/lin-junyang-article-pro.md` | 原文见上一行 | 2026-03-27 |

### AI 使用方法与思维

| 文件 | 主题 | 来源 | 日期 |
|---|---|---|---|
| [Abdaal_How-to-Learn-AI-pro.md](Abdaal_How-to-Learn-AI-pro.md) | AI 流利度五阶段、10-80-10 委托规则、提示词库、自动化层级 | [YouTube·Ali Abdaal](https://www.youtube.com/watch?v=j0YENi6U0tE) | 2026-04-02 |

### 产品经理与 AI 工具

| 文件 | 主题 | 来源 | 日期 |
|---|---|---|---|
| [产品经理6大热门Skills-原文.md](产品经理6大热门Skills-原文.md) | 原文全文：6 个面向 PM 场景的 Skill 推荐；结构化整理在 [`skill-read-collect/pm-6-skills.md`](skill-read-collect/pm-6-skills.md) | [微信公众号](https://mp.weixin.qq.com/s/7fGefu_z9pfBJ5KqkST3Aw) · 留档 `bottleX/url-to-md/mp.weixin.qq.com/6-skills.md` | 2026-03-18 |

### 组织与管理

| 文件 | 主题 | 来源 | 日期 |
|---|---|---|---|
| [AI-native组织.html](AI-native组织.html) | 《如何打造 AI-native 组织》阅读页 | 未记录 | 2026-08-12 |

### 心态与成长

| 文件 | 主题 | 来源 | 日期 |
|---|---|---|---|
| [相信自己而非结果.md](相信自己而非结果.md) | 把苦难当课题、删除受害者标签、做流程主义者 | [微信·智慧少女派](https://mp.weixin.qq.com/s/vQI4kEarQr9UyJ04PifPpQ) · 留档 `bottleX/url-to-md/mp.weixin.qq.com/降低结果渴望提高自我崇拜.md` | 2026-09-08 |

## 成套集合

| 目录 | 内容 |
|---|---|
| [skill-read-collect/](skill-read-collect/) | Skill 相关的阅读整理（firecrawl / gstack / PM 6 skills / follow-builders） |
| [translate-CN/](translate-CN/) | 翻译相关素材与提示词（bilibili-cli、plan-ceo-review、pm_ai_prompts 等） |
| [LsAssets/](LsAssets/) | 个人素材：草稿、笔记提示词、AI 工作日志、图片 |

> **同步**：`tools/bottle_Script/sync_bottle_files.sh` 把本目录镜像推到公开仓库（本地删除的文件远端也会删除） [2bottlepapa/bottle_files](https://github.com/2bottlepapa/bottle_files) 的 `notes/` 下，只排除 `LsAssets/` 和 `translate-CN/`。放进本目录的其他内容都会公开，注意不要放私人素材。

## 约定

- 单篇笔记直接放本目录，**不按来源站点建子目录**；文件名用中文，一眼可读
- 新增单篇笔记按主题登记到对应分类表，没有贴切分类就新开一个三级标题，并更新分类总览的篇数
- 笔记可以是 `.md` 或 `.html`，登记方式相同
- 分类按"这篇笔记回答什么问题"划分，不按来源平台、不按谁生成划分
- 原文与加工版分开放时，在表里注明另一份在哪，避免重复整理
- 网页抓取的**原始产物**（Markdown + 图片目录）统一留在 `~/Documents/bottleX/url-to-md/`（baoyu-url-to-markdown 的默认输出目录，按域名分子目录），只有值得反复读的**全文**才提升到这里
- 整理笔记有两处：本目录（notes-remaker 默认输出目录）和 `~/Documents/bottleX/cc_notes/`（目前都是 AI / Agent 主题），两处的分工规则待定，暂按手动归置
