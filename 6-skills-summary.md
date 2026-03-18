# 产品经理 6 大热门 Skills 信息整理

来源文章：[6-skills.md](./6-skills.md)

本文基于原文内容，对 6 个面向产品经理场景的热门 Skill 进行结构化整理，便于快速查看用途、安装方式和适用场景。

## 总览

| Skill 名称         | 主要用途                             | 作者               | 仓库地址                                         |
| ------------------ | ------------------------------------ | ------------------ | ------------------------------------------------ |
| brainstorming      | 方案头脑风暴、需求澄清、设计方案推演 | obra (superpowers) | https://github.com/obra/superpowers              |
| write-a-prd        | 访谈式 PRD 撰写                      | mattpocock         | https://github.com/mattpocock/skills             |
| writing-plans      | 将方案拆解为可执行实施计划           | obra (superpowers) | https://github.com/obra/superpowers              |
| ab-test-setup      | A/B 实验设计与样本量规划             | coreyhaines31      | https://github.com/coreyhaines31/marketingskills |
| analytics-tracking | 数据埋点与追踪方案设计               | coreyhaines31      | https://github.com/coreyhaines31/marketingskills |
| onboarding-cro     | 新用户激活与 Onboarding 优化         | coreyhaines31      | https://github.com/coreyhaines31/marketingskills |

## 1. brainstorming

- 定位：帮助把模糊想法通过结构化对话转化为清晰设计方案。
- 作者：obra (superpowers)
- 仓库地址：https://github.com/obra/superpowers
- 核心能力：
  - 以一次只问一个问题的方式逐步厘清需求。
  - 主动提出 2 到 3 个可行方案并给出推荐理由。
  - 最终可产出包含架构、数据流、测试策略的完整设计文档。
- 适用场景：
  - 产品新功能概念评审
  - 业务流程再设计
  - 高不确定性的创新项目
  - 内部评审准备
- 安装命令：

```bash
npx skills add obra/superpowers --skill brainstorming
```

- 示例提问：
  - 我想做一个 AI 写作助手，帮我头脑风暴一下产品形态
  - 我们的用户激活率很低，帮我想想新手引导流程该怎么设计
  - 帮我分析这个功能的三种实现方案并给出建议

## 2. write-a-prd

- 定位：面向产品经理的 PRD 撰写 Skill，通过深度访谈生成结构化需求文档。
- 作者：mattpocock
- 仓库地址：https://github.com/mattpocock/skills
- 核心能力：
  - 不是简单套模板，而是通过访谈式对话逐步澄清需求。
  - 像评审一样持续追问关键设计分支和边界条件。
  - 最终输出可直接作为 GitHub Issue 提交的 PRD 文档。
- 输出结构通常包括：
  - 从用户视角描述问题
  - 从用户视角描述解决方案
  - 用户故事类型
  - 模块、接口和架构信息
  - 测试范围与测试策略
  - 其他补充内容
- 适用场景：
  - 新功能需求编写
  - 评审前对齐
  - 跨部门沟通
  - 迭代记录留档
- 安装命令：

```bash
npx skills add mattpocock/skills --skill write-a-prd
```

- 示例提问：
  - 我想做一个用户等级体系，包括积分、勋章和特权，帮我写一份 PRD
  - 帮我把这个功能想法梳理成 PRD，我希望解决的问题是：用户无法感知到自己的成长路径

## 3. writing-plans

- 定位：把需求设计方案拆解成极细颗粒度的执行计划。
- 作者：obra (superpowers)
- 仓库地址：https://github.com/obra/superpowers
- 核心能力：
  - 将复杂目标拆成每步仅需 2 到 5 分钟的微任务。
  - 每一步都可包含明确文件路径、命令和验收预期。
  - 适合把方案沉淀成具备执行顺序和验收标准的任务清单。
- 典型输出内容：
  - 功能目标
  - 架构说明
  - 技术栈
  - 文件结构图
  - 分步骤检查清单
- 适用场景：
  - 项目分解
  - 内容发布计划
  - 与研发沟通时提供开发视角计划草稿
  - 与 brainstorming 配合，方案确认后衔接实施计划
- 安装命令：

```bash
npx skills add obra/superpowers --skill writing-plans
```

- 示例提问：
  - 帮我把用户增长平台这个设计方案直接拆分成可执行的不同计划

## 4. ab-test-setup

- 定位：A/B 实验设计 Skill，强调统计严谨性和结果可操作性。
- 作者：coreyhaines31
- 仓库地址：https://github.com/coreyhaines31/marketingskills
- 核心能力：
  - 覆盖假设框架、样本量计算、指标选择、实验执行规范和结果解读。
  - 帮助避免伪实验、过早停止实验等常见问题。
  - 适合增长、转化率优化和灰度实验场景。
- 适用场景：
  - 页面转化率优化
  - 功能上线灰度实验
  - 文案和视觉元素测试
  - 定价测试
- 安装命令：

```bash
npx skills add coreyhaines31/marketingskills --skill ab-test-setup
```

- 示例提问：
  - 我想测试把注册按钮从蓝色换成橙色，帮我设计一个 A/B 实验
  - 我们的定价页转化率是 3%，我想测试一个新的价值主张，需要多少样本量？

## 5. analytics-tracking

- 定位：埋点方案设计与 Analytics 实施 Skill，用于建立决策导向的数据体系。
- 作者：coreyhaines31
- 仓库地址：https://github.com/coreyhaines31/marketingskills
- 核心能力：
  - 覆盖事件命名规范、追踪计划文档、GTM 配置、UTM 参数策略和隐私合规。
  - 强调围绕业务决策设计数据体系，而不是单纯收集数据。
  - 适合增长分析、漏斗分析和营销归因设计。
- 适用场景：
  - 新功能上线前的产品埋点方案设计
  - A/B 测试事件追踪方案设计
  - Onboarding 漏斗分析
  - 营销归因与统一渠道命名规范
- 安装命令：

```bash
npx skills add coreyhaines31/marketingskills --skill analytics-tracking
```

- 示例提问：
  - 请帮我依据这一份方案制定完整的数据漏斗追踪计划

## 6. onboarding-cro

- 定位：专注新用户激活全链路优化的 Skill。
- 作者：coreyhaines31
- 仓库地址：https://github.com/coreyhaines31/marketingskills
- 核心能力：
  - 帮助识别用户的 Aha 时刻。
  - 设计让用户尽快到达首次成功体验的 Onboarding 流程。
  - 支持搭建多渠道激活运营体系。
- 适用场景：
  - 提升新用户激活率
  - 空白状态设计优化
  - 注册后触发式邮件节点设计
  - 激活环节实验设计
- 安装命令：

```bash
npx skills add coreyhaines31/marketingskills --skill onboarding-cro
```

- 示例提问：
  - 这些留存用户做了哪些动作，而流失用户没有做？

## 安装方式补充

原文还补充了在 TRAE 中安装 Skill 的两种方式：

### 方式一：手动导入

1. 前往 Setting。
2. 在 Rules & Skills 菜单中的 Skills 部分点击创建。
3. 上传 SKILL.md 文件，或上传包含 SKILL.md 的 zip 文件。

### 方式二：命令行导入

可直接在终端执行安装命令，将指定 Skill 添加到 TRAE。

示例命令：

```bash
npx skills add https://github.com/remotion-dev/skills --skill remotion-best-practices
```

注意事项：

- 安装目标需要选择 TRAE 或 TRAE CN。
- 在选择界面中，需要先使用空格选中，再按回车确认。

## 简要结论

这 6 个 Skill 基本覆盖了产品经理从想法形成到执行落地、再到实验和数据追踪的关键环节：

- brainstorming：适合前期想法发散和方案收敛
- write-a-prd：适合把想法沉淀成正式需求文档
- writing-plans：适合把方案继续拆成执行计划
- ab-test-setup：适合设计严谨的实验方案
- analytics-tracking：适合搭建完整的数据追踪体系
- onboarding-cro：适合优化新用户激活和留存起点
