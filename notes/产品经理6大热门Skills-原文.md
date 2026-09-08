---
url: https://mp.weixin.qq.com/s/7fGefu_z9pfBJ5KqkST3Aw?click_id=39
title: "产品经理 6 大热门 Skills 推荐"
author: "TRAE"
coverImage: "https://mmbiz.qpic.cn/mmbiz_jpg/5lJ4HUd9eVPGA1mN9OWQguouCibgxBV64iciafMdodRGIUIVKjsHQl9jzujh9RicicCJeckKjfib6ib7UC8DHOGg7fXOznZtcs9vibiaVWv0zZxx8lfk/0?wx_fmt=jpeg"
captured_at: "2026-03-18T09:36:12.777Z"
---

# 产品经理 6 大热门 Skills 推荐

原创 TRAE *2026年3月17日 20:06*

本文作者：小菠，TRAE 用户运营

产品从 0 到 1 的孵化，再到持续迭代演进，是一项需要多角色协同的系统工程。除研发团队外，产品经理、运营、数据分析、UI/UX 设计等角色均深度参与其中。在与 TRAE 用户的日常交流中，我们发现越来越多的产品经理正在将 TRAE IDE 融入其工作流。

基于此，我们精选整理了 6 款面向产品经理场景的热门 Skills，覆盖从方案设计、实施拆解到上线后数据追踪的全链路环节，助力产品经理在各关键节点提升工作效率。

![图片](https://mmbiz.qpic.cn/mmbiz_png/5lJ4HUd9eVPSIwpHlojR7pBPY9XB3wX9uSibdAibl2MCf9wWa3LMuFvFicicUSsVvl72fBoBqnfanxmDLHh9qU9IL6szBqHiaciaK4Lz1CcdVRoLU/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**方案头脑风暴**

**名称**

brainstorming

**作者**

obra( superpowers)

**地址**

https://github.com/obra/superpowers

**描述说明**

这个 Skill 可以帮助你将模糊想法通过结构化对话转化为清晰设计方案。

以"一次只问一个问题"的方式，像资深产品顾问一样逐步厘清需求，主动提出 2-3 个可行方案并给出有理由的推荐，最终产出包含架构、数据流、测试策略的完整设计文档。

**安装命令**

```sql
npx skills add obra/superpowers --skill brainstorming
```

**应用场景**

- **产品新功能概念评审：** 在写 PRD 之前，先通过对话发散思路、收敛方案
- **业务流程再设计：** 梳理复杂业务逻辑，从多角度提出优化方向
- **不确定性高的创新项目：** 适合"我有一个方向但不知道怎么落地"的场景
- **内部评审准备：** 借助 AI 提前模拟评审追问，堵住方案漏洞

**使用举例**

```js
“我想做一个 AI 写作助手，帮我头脑风暴一下产品形态”“我们的用户激活率很低，帮我想想新手引导流程该怎么设计”“帮我分析这个功能的三种实现方案并给出建议”
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/5lJ4HUd9eVNbCicfDKNZndqTyYrCFTpB0UdNmXESATk9WFS0XgWTYwnmibTzrfXQicd1Ql0GuBibJbIj2jianiaKK9XmsbWRgJwmx576FyZMhJt9A/640?wx_fmt=png&from=appmsg#imgIndex=2)

**需求设计**

**名称**

write-a-prd

**作者**

mattpocock

**地址**

https://github.com/mattpocock/skills

**描述说明**

这是一个专为产品经理量身定制的 PRD（产品需求文档）撰写 Skill。它不是简单地填写模板，而是通过与用户进行深度对话式访谈，逐步厘清需求全貌，然后产出一份经过严格结构化的、可直接作为 GitHub Issue 提交的 PRD 文档。

这个 Skill 采用“访谈式” 的工作模式：它会先让你详细描述问题和方案想法，再像产品评审一样对每个设计分支追问到底，直到达成共同理解，最终生成一份 PRD 文档。

它整体的 PRD 文档结构如下：

1. 从用户视角描述面临的问题
2. 从用户视角描述解决方案
3. 列举详细的用户故事类型
4. 模块划分、接口设计、架构等信息
5. 测试范围、测试策略推荐
6. 其他需要补充的内容

**安装命令**

```css
npx skills add mattpocock/skills --skill write-a-prd
```

**应用场景**

- **新功能需求编写：** 从一个模糊想法出发，通过对话逐步形成完整、可执行的 PRD
- **评审前对齐：** 借助 AI 充当"审稿人"，在提交评审前提前暴露逻辑漏洞和边界遗漏 Case
- **跨部门沟通：** 生成用户故事驱动的需求文档，让研发和设计更容易理解用户价值
- **迭代记录：** 每个功能点都形成可追溯的历史记录

**使用举例**

```js
“我想做一个用户等级体系，包括积分、勋章和特权，帮我写一份 PRD”“帮我把这个功能想法梳理成 PRD，我希望解决的问题是：用户无法感知到自己的成长路径”
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5lJ4HUd9eVMcFmfhHqCaSd6t66ENdtSntaVGueBfFzpVt5P76hPBzibqO9cKialZ5JKsWugACK5X4E4QN6A5ttJUEdGjHlibag0GMFnA6bEeias/640?wx_fmt=png&from=appmsg#imgIndex=3)

**实施计划拆分**

**名称**

writing-plans

**作者**

obra( superpowers)

**地址**

https://github.com/obra/superpowers

**描述说明**

这是一款将需求设计方案拆解为极细颗粒度执行计划的 Skill。

每个步骤仅需 2-5 分钟，包含明确的文件路径、命令和验收预期。虽然原本设计用于研发实施，但其"把复杂目标拆解成带验收标准的微任务清单"的核心能力，同样适用于产品经理规划项目执行路径、制定内容发布计划，或在与研发对齐时提供细粒度任务分解参考。

每份计划文档包含：功能目标（一句话）、架构说明（2-3 句）、技术栈、文件结构 Map，以及每个任务块的分步骤检查清单（含代码、命令、预期输出）。

**安装命令**

```sql
npx skills add obra/superpowers --skill writing-plans
```

**应用场景**

- **项目分解：** 将一个产品大需求拆解为可追踪、有顺序的执行子任务
- **内容发布计划：** 每个节点明确产出物、负责人、验收标准
- **与研发沟通：** 产出一份开发视角的实施计划草稿，供研发评估工作量
- **配合 brainstorming skill（头脑风暴）使用：** 方案确认后，自动衔接生成实施计划

**使用举例**

```js
“帮我把用户增长平台这个设计方案直接拆分成可执行的不同计划”
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/5lJ4HUd9eVMF7LpkxDsQ7GxONy0jOYH9sPV0bBicibdJK1K4CKePemGaQCqLq4ADKkbdH7Laoz0FJCU1HVRr6N3n4OaiaHWiavt4rUh9pibQ9YAQ/640?wx_fmt=png&from=appmsg#imgIndex=4)

**A/B 实验设计**

**名称**

ab-test-setup

**作者**

coreyhaines31

**地址**

https://github.com/coreyhaines31/marketingskills

**描述说明**

这是一款专业的 A/B 实验设计 Skill，帮助产品经理和增长团队设计统计上严格、结果可操作的实验。从假设框架、样本量计算、指标选择，到实验执行规范和结果解读，全链路覆盖，避免"伪实验"和"早停问题"等常见陷阱。

**安装命令**

```sql
npx skills add coreyhaines31/marketingskills --skill ab-test-setup
```

**应用场景**

- **页面转化率优化：** 落地页、注册流程、付费页面的 A/B 实验方案设计
- **功能上线灰度：** 新功能对照实验，评估用户行为变化
- **文案/视觉测试：** 标题、CTA、图片等创意元素的对比测试
- **定价测试：** 不同定价展示方式的转化率实验

**使用举例**

```css
“我想测试把注册按钮从蓝色换成橙色，帮我设计一个 A/B 实验”“我们的定价页转化率是 3%，我想测试一个新的价值主张，需要多少样本量？”
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/5lJ4HUd9eVMNH3mlGia6PIfQCwxibQ6hASPS4liaVcHKmQDS45qffSRelYNZPPlObSN5TJTYFRve7KxwhOL4OeeghiaAqATTekoOqmJakjic0TO0/640?wx_fmt=png&from=appmsg#imgIndex=5)

**数据埋点与追踪**

**名称**

analytics-tracking

**作者**

coreyhaines31

**地址**

https://github.com/coreyhaines31/marketingskills

**描述说明**

这是一款埋点方案设计与 Analytics 实施的专家级 Skill，覆盖事件命名规范、追踪计划文档、GTM 配置、UTM 参数策略和隐私合规的完整方法论，帮助产品和增长团队建立 **以决策为导向的数据体系** ，而非为了收集数据而收集数据。

**安装命令**

```sql
npx skills add coreyhaines31/marketingskills --skill analytics-tracking
```

**应用场景**

- **产品埋点方案设计：** 新功能上线前，制定完整的追踪计划文档
- **增长实验追踪：** 为 A/B 测试设计事件追踪方案
- **Onboarding 漏斗分析：** 追踪每个激活步骤的转化率
- **营销归因设置：** 配置 UTM 策略，建立统一的渠道命名规范

**使用举例**

```js
“请帮我依据这一份方案制定完整的数据漏斗追踪计划”
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5lJ4HUd9eVOYbzZ7XcDpTvqCqVAUbBdWxHjWicaia3XKjxcNNJCF2gesV4JK2psNXX89jLmict40Pg1CgefACaNez0blnTdm2uI96icar7BZHqY/640?wx_fmt=png&from=appmsg#imgIndex=6)

**新用户激活**

**名称**

onboarding-cro

**作者**

coreyhaines31

**地址**

https://github.com/coreyhaines31/marketingskills

**描述说明**

这是一款专注于新用户激活全链路优化的 Skill，帮助产品经理找到“用户 Aha 时刻”，设计让用户尽快到达第一个成功体验的 Onboarding 流程，并搭建多渠道的激活运营体系。

**安装命令**

```sql
npx skills add coreyhaines31/marketingskills --skill onboarding-cro
```

**应用场景**

- **新激活率提升：** 系统分析当前 Onboarding 漏斗，找到最大流失节点
- **空白状态设计：** 把"空页面"变成用户激活的引导机会
- **Onboarding 邮件触达设计：** 设计注册后的触发式邮件时间节点（24h/72h/Day 7）
- **激活实验设计：** 识别哪些 Onboarding 步骤值得 A/B 测试

**使用举例**

```js
“这些留存用户做了哪些动作，而流失用户没有做？”
```

**如何在 TRAE 内安装？**

![图片](https://mmbiz.qpic.cn/mmbiz_png/5lJ4HUd9eVND2VGVyeljGNarJ7f0xAS9GptfyVze2W8XibvicDLNSep2YWKtsHFux6H0RgTgrVXfLwySCwSSfF4seyLXdRZgdyW3skfLJRvE0/640?wx_fmt=png&from=appmsg#imgIndex=7)

那推荐了这么多 Skill，你应该如何在 TRAE 中使用呢。

**方法一：手动导入一个 Skills**

若你需要使用外部已创建的技能，可以直接将 SKILL.md 文件或包含 SKILL.md 以及其他相关文件的.zip 文件导入至 TRAE。

我们在每个推荐的 Skill 都放上了 Github 的下载地址，大家可以直接下载 Skill 的 Zip 包即可。

1. 前往 Setting 设置 。
2. 在 Rules & Skills 菜单栏下的 Skills 部分，点击 **创建** 按钮。
3. 在弹出窗口中，上传一个 SKILL.md 文件或一个包含 SKILL.md 文件的.zip 文件，然后确认。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/5lJ4HUd9eVOtvPJ6AlqicWWCta4DEPkFhoBBwBWibQu9HThfVDskaTaO9yiaBhmkydibg8QibMYf5maMjpAWMdGefRq8XibZskHqHyian5via49hgoE/640?wx_fmt=png&from=appmsg#imgIndex=8)

**方法二：命令行中导入外部 Skills**

TRAE 同样可以从命令行中导入外部 Skills，并选择应用于全局或是当前项目。

比如如果我们要为当前项目添加一个 Brainstorming Skills，可以使用命令行安装，直接把下面的指令复制粘贴到 TRAE 的终端里面

```cs
npx skills add https://github.com/remotion-dev/skills --skill remotion-best-practices
```

在 "Which agents do you want to install to"， 选择 "TRAE" （国际版）或 “TRAE CN” （国内版）:

**【注意：要通过空格的方式选中 TRAE 或 TRAE CN（space select），选中后再按回车进入下一步（enter confirm），否则不会安装到 TRAE 中】**

你还期望获得哪个场景的 Skill 推荐呢？官方通通帮你搞定！欢迎在评论区积极留言，让我们听到各行各业小伙伴的声音！

更多干货和实战案例，可点击 **阅读全文** ，前往 TRAE 官方中文社区发现和讨论～

![图片](https://mmbiz.qpic.cn/mmbiz_png/5lJ4HUd9eVPiaApcC56JZSaS8NBP1aMXv3jQ6eo3cic5ky4BS6cvkPjiaaCRgacVPWbvQib3TWLoBEQDxotgo4gtItEggeXNaf1ltmNyKXR2d2U/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

阅读原文

继续滑动看下一个

TRAE.ai

向上滑动看下一个
