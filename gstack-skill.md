# 技能深度解析

gstack（作者自建的 AI 编码代理系统框架）每项技能（skill）的详细指南——理念、工作流程与示例。

| 技能 | 你的专家角色 | 职责 |
|-------|----------------|--------------|
| [`/plan-ceo-review`](#plan-ceo-review) | **CEO / 创始人** | 重新思考问题。发掘需求背后隐藏的十星级产品。四种模式（mode）：范围扩展（Scope Expansion）、选择性扩展（Selective Expansion）、保持范围（Hold Scope）、范围缩减（Scope Reduction）。 |
| [`/plan-eng-review`](#plan-eng-review) | **工程经理** | 锁定架构、数据流、图表、边界情况（edge case）和测试。将隐含假设全部暴露出来。 |
| [`/plan-design-review`](#plan-design-review) | **资深设计师** | 交互式方案阶段设计评审。对每个维度评分 0-10，解释 10 分是什么样子，然后修正方案。在方案阶段工作。 |
| [`/design-consultation`](#design-consultation) | **设计合伙人** | 从零开始构建完整的设计系统。了解行业现状，提出创造性的冒险方案，生成逼真的产品原型。设计贯穿所有阶段的核心。 |
| [`/review`](#review) | **Staff 工程师** | 找出那些能通过 CI 却会在生产环境中"炸雷"的 bug。自动修复显而易见的问题，标记完整性缺口。 |
| [`/ship`](#ship) | **发布工程师** | 同步 main 分支、运行测试、审查覆盖率（coverage）、推送、创建 PR。如果没有测试框架会自动引导建立。一条命令搞定。 |
| [`/browse`](#browse) | **QA 工程师** | 给代理（agent）装上"眼睛"。真正的 Chromium 浏览器，真实的点击，真实的截图。每条命令约 100ms。 |
| [`/qa`](#qa) | **QA 负责人** | 测试你的应用，发现 bug，用原子提交（atomic commit）修复，再次验证。为每个修复自动生成回归测试（regression test）。 |
| [`/qa-only`](#qa) | **QA 报告员** | 与 /qa 方法论相同，但仅输出报告。适用于你只想要一份纯粹的 bug 报告、不需要代码变更的场景。 |
| [`/design-review`](#design-review) | **懂代码的设计师** | 线上站点视觉审查 + 修复循环。80 项审查清单，然后修复发现的问题。原子提交，附带修复前后的截图对比。 |
| [`/setup-browser-cookies`](#setup-browser-cookies) | **会话管理器** | 从你实际使用的浏览器（Chrome、Arc、Brave、Edge）导入 cookie 到无头浏览器（headless browser）会话。测试需要登录的页面。 |
| [`/retro`](#retro) | **工程经理** | 团队维度的周复盘。按人拆解、发布连续性追踪、测试健康趋势、成长机会。 |
| [`/document-release`](#document-release) | **技术文档工程师** | 更新所有项目文档以匹配你刚发布的内容。自动捕捉过时的 README。 |

---

## `/plan-ceo-review`

这是我的**创始人模式**。

在这个模式下，我希望模型带着品味、野心、用户同理心和长远眼光来思考。我不希望它死板地按字面意思理解需求。我希望它先问一个更重要的问题：

**这个产品到底是为了什么？**

我把这称为 **Brian Chesky 模式**（Brian Chesky，Airbnb 联合创始人，以"十星级体验"产品设计理念闻名）。

重点不是实现那张显而易见的工单。重点是从用户的视角重新审视问题，找到那个让人觉得理所当然、令人愉悦、甚至有一点魔力的版本。

### 示例

假设我在开发一个类似 Craigslist 的商品发布应用，我说：

> "让卖家可以为商品上传一张照片。"

一个平庸的助手会加一个文件选择器，保存一张图片。

那不是真正的产品。

在 `/plan-ceo-review` 中，我希望模型去追问"上传照片"是否真的就是那个核心功能。也许真正的功能是帮助用户创建一条真正能卖出去的商品信息。

如果那才是真正的任务，整个方案就要彻底改变。

现在模型应该去思考：

* 我们能从照片中识别出产品吗？
* 我们能推断出 SKU 或型号吗？
* 我们能搜索网络并自动起草标题和描述吗？
* 我们能拉取规格、类目和价格对比数据吗？
* 我们能推荐哪张照片最适合作为主图来提升转化率吗？
* 我们能检测出上传的照片是不是太暗、太杂乱、画质差或缺乏信任感吗？
* 我们能让整个体验感觉高端，而不是像 2007 年的僵尸表单吗？

这就是 `/plan-ceo-review` 为我做的事。

它不只是问"我要怎么加这个功能？"
它问的是：**"这个需求背后隐藏的十星级产品是什么？"**

### 四种模式

- **范围扩展（SCOPE EXPANSION）**——大胆想象。代理提出雄心勃勃的版本。每项扩展都作为一个独立的决策供你选择。会热情地推荐。
- **选择性扩展（SELECTIVE EXPANSION）**——以当前范围为基线，但展示还有哪些可能性。代理逐一呈现机会，给出中性的建议——你挑选值得做的。
- **保持范围（HOLD SCOPE）**——对现有方案保持最大严谨性。不呈现任何扩展。
- **范围缩减（SCOPE REDUCTION）**——找到最小可行版本。砍掉其他一切。

愿景和决策会持久存储到 `~/.gstack/projects/`，跨对话保留。出色的愿景可以提升到代码仓库中的 `docs/designs/` 供团队共享。

---

## `/plan-eng-review`

这是我的**工程经理模式**。

产品方向确定之后，我需要的是完全不同的一种智慧。我不要更多漫无边际的头脑风暴。我不要更多"要是能……岂不是很酷"。我要模型变成我最好的技术负责人。

这个模式应该精准把握：

* 架构
* 系统边界
* 数据流
* 状态转换
* 故障模式
* 边界情况
* 信任边界（trust boundary）
* 测试覆盖率

还有一个对我来说意外重大的突破：**图表**。

当你强制 LLM 把系统画出来时，它们的输出会变得完整得多。时序图、状态图、组件图、数据流图，甚至测试矩阵。图表会把隐含假设全部暴露出来。它们让含糊其辞的规划无处遁形。

所以 `/plan-eng-review` 就是我希望模型来构建技术骨架的地方——一个能支撑产品愿景的技术骨架。

### 示例

还是拿那个商品发布应用举例。

假设 `/plan-ceo-review` 已经完成了它的工作。我们决定真正的功能不只是上传照片，而是一个智能发布流程：

* 上传照片
* 识别产品
* 从网络进行信息补充（enrichment）
* 起草一个有力的标题和描述
* 推荐最佳主图

现在 `/plan-eng-review` 接管。

现在我希望模型来回答这些问题：

* 上传、分类、信息补充和草稿生成的架构是什么？
* 哪些步骤是同步执行的，哪些进后台任务？
* 应用服务器、对象存储、视觉模型、搜索/信息补充 API 和商品数据库之间的边界在哪里？
* 如果上传成功但信息补充失败怎么办？
* 如果产品识别的置信度很低怎么办？
* 重试机制怎么设计？
* 如何防止重复任务？
* 什么时候持久化什么数据？什么可以安全地重新计算？

这就是我需要图表的地方——架构图、状态模型、数据流图、测试矩阵。图表会把隐含假设全部暴露出来。它们让含糊其辞的规划无处遁形。

这就是 `/plan-eng-review`。

不是"把想法做小"。
而是**让想法变得可落地**。

### 评审就绪仪表盘

每次评审（CEO、Eng、Design）都会记录其结果。每次评审结束时，你会看到一个仪表盘（dashboard）：

```
+====================================================================+
|                    REVIEW READINESS DASHBOARD                       |
+====================================================================+
| Review          | Runs | Last Run            | Status    | Required |
|-----------------|------|---------------------|-----------|----------|
| Eng Review      |  1   | 2026-03-16 15:00    | CLEAR     | YES      |
| CEO Review      |  1   | 2026-03-16 14:30    | CLEAR     | no       |
| Design Review   |  0   | —                   | —         | no       |
+--------------------------------------------------------------------+
| VERDICT: CLEARED — Eng Review passed                                |
+====================================================================+
```

Eng Review 是唯一的必要门禁（可通过 `gstack-config set skip_eng_review true` 关闭）。CEO 和 Design 评审是参考性的——分别推荐用于产品变更和 UI 变更。

### 方案到 QA 的流转

当 `/plan-eng-review` 完成测试评审部分后，它会将测试计划工件写入 `~/.gstack/projects/`。当你之后运行 `/qa` 时，它会自动拾取该测试计划——你的工程评审直接输入到 QA 测试中，无需手动复制粘贴。

---

## `/plan-design-review`

这是**我的资深设计师在审查你的方案**——在你写下一行代码之前。

大多数方案描述了后端做什么，但从未指定用户实际看到什么。空状态？错误状态？加载状态？移动端布局？AI 模板化（AI Slop）风险？这些决策被推迟到"实现的时候再说"——然后工程师发布时就拿一句"未找到任何项目。"做空状态，因为根本没人指定更好的方案。

`/plan-design-review` 在规划阶段就捕捉所有这些问题——那时修改成本最低。

它的工作方式和 `/plan-ceo-review`、`/plan-eng-review` 类似——交互式的，一次处理一个问题，采用 **STOP + AskUserQuestion** 模式。它对每个设计维度评分 0-10，解释 10 分是什么样子，然后编辑方案让它达到那个水平。评分驱动工作量：评分低 = 大量修复，评分高 = 快速通过。

对方案进行七轮审查：信息架构、交互状态覆盖、用户旅程、AI 模板化风险、设计系统一致性、响应式/无障碍性，以及未解决的设计决策。对于每一轮，它找到问题然后要么直接修复（显而易见的问题），要么请你做出设计选择（真正的权衡取舍）。

### 示例

```
You:   /plan-design-review

Claude: Initial Design Rating: 4/10

        "This plan describes a user dashboard but never specifies
         what the user sees first. It says 'cards with icons' —
         which looks like every SaaS template. It mentions zero
         loading states, zero empty states, and no mobile behavior."

        Pass 1 (Info Architecture): 3/10
        "A 10 would define primary/secondary/tertiary content
         hierarchy for every screen."
        → Added information hierarchy section to plan

        Pass 2 (Interaction States): 2/10
        "The plan has 4 UI features but specifies 0 out of 20
         interaction states (4 features × 5 states each)."
        → Added interaction state table to plan

        Pass 4 (AI Slop): 4/10
        "The plan says 'clean, modern UI with cards and icons'
         and 'hero section with gradient'. These are the top 2
         AI-generated-looking patterns."
        → Rewrote UI descriptions with specific, intentional alternatives

        Overall: 4/10 → 8/10 after fixes
        "Plan is design-complete. Run /design-review after
         implementation for visual QA."
```

当你再次运行时，已经达到 8+ 分的部分会快速通过。低于 8 分的部分会进行完整处理。实现后的线上站点视觉审查，请使用 `/design-review`。

---

## `/design-consultation`

这是我的**设计合伙人模式**。

`/plan-design-review` 审查的是一个已经存在的站点。`/design-consultation` 针对的是你什么都还没有的情况——没有设计系统，没有字体选择，没有调色板。你从零开始，希望一位资深设计师坐下来和你一起构建整个视觉识别体系。

这是一次对话，不是一张表单。代理会询问你的产品、你的用户和你的受众。它会思考你的产品需要传达什么——信任、速度、匠心、温度，或者其他合适的感觉——然后从这些目标反推到具体的设计选择。接着它会提出一个完整的、一致的设计系统：美学方向、字体排印（3 种以上字体并具有明确的角色分工）、带十六进制色值的调色板、间距刻度、布局策略和动效策略。每个推荐都附带理由。每个选择都与其他选择相互强化。

但一致只是基本功。每个开发者工具的仪表盘看起来都一样——简洁的无衬线字体、柔和的灰色、一个蓝色强调色。它们都很一致。它们都毫无辨识度。一个"看着不错"的产品和一个让人真正记住的产品之间的区别在于**有意为之的创造性冒险**：标题使用出乎意料的衬线字体，采用同类产品中无人使用的大胆强调色，以更紧凑的间距让数据感觉更权威而非更空旷。

这才是 `/design-consultation` 真正要做的事。它不只是提出一个安全的系统。它同时提出安全的选择和冒险的选择——并告诉你哪些是哪些。"这些选择让你在品类中不会显得格格不入。而这里是我认为你应该打破常规的地方，以及为什么。"你来选择承担哪些风险。代理会检查整个系统无论如何都依然协调一致。

如果你愿意，代理会调研你所在领域的现有产品——对真实网站截图，分析它们的字体、颜色和间距——让你在做选择之前先了解行业现状。这不是为了抄袭。而是为了先摸清约定俗成的做法，然后再决定哪些值得打破。

当你确定了设计系统后，它会生成一个交互式 HTML 预览页面——不只是色板和字体样本，而是逼真的产品页面。如果你在做仪表盘，你看到的就是一个带侧边栏、数据表格和统计卡片的仪表盘。如果你在做营销网站，你看到的就是带真实文案和 CTA 的首屏区域。所有内容都用你的设计系统渲染，使用你的产品名称，同时支持亮色和暗色模式。你可以在写一行生产代码之前就感受到你的产品可能呈现的样子。

然后它会将 `DESIGN.md` 写入你的代码仓库根目录——作为项目的设计唯一真相来源——并更新 `CLAUDE.md`，使得未来每个 Claude Code 会话都遵守这套设计系统。从此以后，`/design-review` 可以据此审查，任何参与前端工作的代理都知道规则。

### 示例

```
You:   /design-consultation

Claude: From the README, this looks like a developer analytics dashboard
        for engineering teams. Sound right? Tell me about the feeling
        you want — and would you like me to look at what's out there
        first so we can see the landscape?

You:    Yes, it's for eng managers. Show me what's out there.

Claude: [browses Linear, Vercel, Datadog, Posthog — takes screenshots]

        Here's the landscape. They all converge on clean sans-serifs
        and muted blue-gray palettes. Linear stands out with dark-first
        and tight spacing. The rest feel interchangeable.

        Here's my proposal — and where I'd play it safe vs. take risks:

        AESTHETIC: Industrial/Utilitarian — data-first, every pixel earns its place
        TYPOGRAPHY: Geist (body + UI), Instrument Serif (display), JetBrains Mono (data)
        COLOR: Restrained — slate neutrals, single teal accent (#0D9488)
        SPACING: 4px base, compact density
        LAYOUT: Grid-disciplined, 12-column
        MOTION: Minimal-functional — only transitions that aid comprehension

        SAFE CHOICES (match category expectations):
          Geist for body — your users already know this font from Vercel
          Slate neutrals — warm grays feel right for data-heavy UIs
          Grid-disciplined layout — dashboards need predictable alignment

        RISKS (where you'd stand out):
          Instrument Serif for display headings — nobody in dev tools
            uses a serif. It creates instant hierarchy contrast and
            signals "we care about craft" in a space full of sans-serifs.
          Single teal accent instead of blue — everyone else in this space uses blue.
            Teal is close enough to feel trustworthy, different enough
            to be recognizable.
          4px compact density — tighter than Linear, says "we respect
            your screen real estate."

        The safe choices keep you literate. The risks are where your
        product gets its own face. Which risks appeal to you?

You:    Love the serif risk. Let's see it.

Claude: Preview opened in your browser.
        [/tmp/design-consultation-preview-1710000000.html]

        The page shows a realistic dashboard: sidebar nav, header with
        avatar, stat cards, data table — all in your design system.
        Instrument Serif at hero scale, Geist in body text, JetBrains
        Mono in the data table. Teal accent on buttons and active states.
        Light and dark mode toggle in the corner.

        How does it feel? Want to adjust anything before I write DESIGN.md?

You:    Ship it.

Claude: Wrote DESIGN.md (typography, color, spacing, layout, motion).
        Updated CLAUDE.md with design system guidelines.
        All future sessions will respect these choices.
```

---
## `/design-review`

这是我的**会写代码的设计师模式**。

`/plan-design-review` 在实施前审查你的计划。`/design-review` 则在上线后对站点进行审计和修复。

它会对你的线上站点执行一项 80 条目的视觉审计，然后进入修复循环：针对每个设计发现，定位源文件，做最小化的 CSS/样式调整，以 `style(design): FINDING-NNN` 格式提交，重新导航验证，并截取修复前后的对比截图。每个修复一次提交，完全可二分定位。

自我调节启发式机制专为设计工作调优——纯 CSS 修改免检放行（天然安全且可逆），但对组件 JSX/TSX 文件的修改会消耗风险预算。硬性上限 30 个修复。风险分数超过 20% 时，它会停下来征求你的意见。

### 示例

```
You:   /design-review https://myapp.com

Claude: [Runs full 80-item visual audit on the live site]
        Design Score: C  |  AI Slop Score: D
        12 findings (4 high, 5 medium, 3 polish)

        Fixing 9 design issues...

        style(design): FINDING-001 — replace 3-column icon grid with asymmetric layout
        style(design): FINDING-002 — add heading scale 48/32/24/18/16
        style(design): FINDING-003 — remove gradient hero, use bold typography
        style(design): FINDING-004 — add second font for headings
        style(design): FINDING-005 — vary border-radius by element role
        style(design): FINDING-006 — left-align body text, reserve center for headings
        style(design): FINDING-007 — add hover/focus states to all interactive elements
        style(design): FINDING-008 — add prefers-reduced-motion media query
        style(design): FINDING-009 — set max content width to 680px for body text

        Final audit:
        Design Score: C → B+  |  AI Slop Score: D → A
        9 fixes applied (8 verified, 1 best-effort). 3 deferred.

        [Report with before/after screenshots saved to .gstack/design-reports/]
```

九次提交，每次只涉及一个关注点。AI 模板化评分（AI Slop Score，作者自定义的指标，衡量设计中 AI 模板化程度）从 D 升到了 A，因为三个最容易辨认的模板化特征（渐变主视觉、三栏网格、统一圆角）都已消除。

---

## `/review`

这是我的**偏执 Staff 工程师模式**。

测试通过不代表分支是安全的。

`/review` 存在的意义在于，有一整类 bug 能躲过 CI，却会在生产环境中"炸雷"。这个模式不是为了描绘更宏大的蓝图，也不是为了让计划更好看。它只问一个问题：

**还有什么会崩？**

这是一场结构性审计，不是风格上的吹毛求疵。我希望模型去关注这些问题：

* N+1 查询（N+1 query）
* 过期读取
* 竞态条件（race condition）
* 不当的信任边界（trust boundary）
* 缺失索引
* 转义缺陷
* 被破坏的不变量
* 不当的重试逻辑
* 测试通过了，却漏掉了真正故障模式的用例
* 遗漏的枚举处理——新增一个状态或类型常量，`/review` 会追踪它在代码库中每一个 switch 语句和白名单中的使用情况，而不仅仅看你改动过的文件

### 修复优先

发现问题就采取行动，而不只是罗列。显而易见的机械性修复（死代码、过期注释、N+1 查询）会自动应用——你会看到每一条 `[AUTO-FIXED] file:line Problem → what was done`。真正存在歧义的问题（安全性、竞态条件、设计决策）则会呈报给你决定。

### 完整性差距

`/review` 还会标记那些走了捷径的实现——前提是完整版方案的成本不超过 30 分钟的 CC 时间。如果你选了 80% 的方案，而 100% 的方案其实只是一条小河，不是大海，审查就会指出来。

### 示例

假设智能上架流程已经实现，测试也全绿了。

`/review` 仍然应该追问：

* 渲染商品照片或草稿建议时，我是否引入了 N+1 查询？
* 我是否在信任客户端提供的文件元数据，而没有验证实际文件？
* 两个标签页是否会产生竞态，覆盖封面图选择或商品详情？
* 上传失败后是否会在存储中留下孤儿文件？
* "恰好一张主图"的规则在并发场景下会不会被打破？
* 如果信息补充（enrichment）API 部分失败，我是优雅降级还是保存了垃圾数据？
* 通过从网络拉取数据来生成草稿时，是否意外制造了提示注入或信任边界问题？

这就是 `/review` 的意义所在。

我不要恭维。
我要模型在生产事故发生之前就预见到它。

---

## `/ship`

这是我的**发布机器模式**。

一旦我决定了要构建什么、敲定了技术方案、做完了认真的审查，我就不想再多说了。我要的是执行。

`/ship` 是为最后一公里而生的。它服务于一个准备就绪的分支，而不是用来讨论该构建什么。

到了这一步，模型应该停止充当头脑风暴伙伴，开始像一名纪律严明的发布工程师那样行事：同步 main 分支，运行正确的测试，确保分支状态正常，按需更新 changelog 或版本号，推送代码，创建或更新 PR。

### 测试引导

如果你的项目还没有测试框架，`/ship` 会帮你搭建——检测运行时环境，调研最佳框架，安装并为你的实际代码编写 3-5 个真实测试，配置 CI/CD（GitHub Actions），并创建 TESTING.md。目标是 100% 测试覆盖率（coverage）——测试让凭感觉编程（Vibe Coding）从"裸奔"变为安全驾驶。

### 覆盖率审计

每次 `/ship` 运行都会根据你的 diff 构建代码路径图，搜索对应的测试，并生成带有质量星级的 ASCII 覆盖率图表。发现的覆盖空白会自动生成测试。你的 PR 描述中会展示覆盖率变化：`Tests: 42 → 47 (+5 new)`。

### 审查门禁

`/ship` 在创建 PR 前会检查[审查就绪仪表盘](#review-readiness-dashboard)（Review Readiness Dashboard）。如果工程审查缺失，它会提醒——但不会阻塞你。决定按分支保存，不会重复询问。

许多分支在有趣的工作完成后就死掉了，因为剩下的只是枯燥的发布流程。人类会拖延这部分，AI 不该如此。

---

## `/browse`

这是我的 **QA 工程师模式**。

`/browse` 是闭合反馈循环的那个技能（skill）。在它出现之前，AI 智能体（AI Agent）能思考也能写代码，但仍然处于半盲状态。它只能猜测 UI 状态、认证流程、重定向、控制台错误、空状态和布局错位。现在它可以直接去看了。

它是一个编译好的二进制文件，与持久化的 Chromium 守护进程通信——基于微软的 [Playwright](https://playwright.dev/)（Playwright，Microsoft 开发的浏览器自动化测试框架）构建。首次调用启动浏览器（约 3 秒），此后每次调用约 100–200 毫秒。浏览器在命令之间保持运行，因此 cookie、标签页和 localStorage 会持续保留。

### 示例

```
You:   /browse staging.myapp.com — log in, test the signup flow, and check
       every page I changed in this branch

Claude: [18 tool calls, ~60 seconds]

        > browse goto https://staging.myapp.com/signup
        > browse snapshot -i
        > browse fill @e2 "test@example.com"
        > browse fill @e3 "password123"
        > browse click @e5                    (Submit)
        > browse screenshot /tmp/signup.png
        > Read /tmp/signup.png

        Signup works. Redirected to onboarding. Now checking changed pages.

        > browse goto https://staging.myapp.com/dashboard
        > browse screenshot /tmp/dashboard.png
        > Read /tmp/dashboard.png
        > browse console

        Dashboard loads. No console errors. Charts render with sample data.

        All 4 pages load correctly. No console errors. No broken layouts.
        Signup → onboarding → dashboard flow works end to end.
```

18 次工具调用，大约一分钟。完整的 QA 测试通过。无需打开浏览器。

**安全提示：**`/browse` 运行的是持久化 Chromium 会话。cookie、localStorage 和会话状态在命令之间会保留。除非你确实有此需要，否则不要用它对接敏感的生产环境——这是一个具有真实状态的真实浏览器。会话在闲置 30 分钟后自动关闭。

完整命令参考请见 [BROWSER.md](../BROWSER.md)。

---

## `/qa`

这是我的 **QA 负责人模式**。

`/browse` 给智能体装上了"眼睛"。`/qa` 则给了它一套测试方法论。

最常见的使用场景：你在一个功能分支上，刚写完代码，想验证一切是否正常。输入 `/qa` 即可——它会读取你的 git diff，识别你的改动影响了哪些页面和路由，启动浏览器，逐一测试。无需提供 URL，无需手写测试计划。

四种模式：

- **Diff 感知模式**（功能分支上自动启用）——读取 `git diff main`，识别受影响的页面，针对性测试
- **完整模式**——系统性探索整个应用，耗时 5–15 分钟，记录 5–10 个有充分证据的问题
- **快速模式**（`--quick`）——30 秒冒烟测试，覆盖首页加前 5 个导航目标
- **回归模式**（`--regression baseline.json`）——运行完整模式，然后与之前的基线进行比对

### 自动回归测试

当 `/qa` 修复了一个 bug 并完成验证后，它会自动生成一个回归测试（regression test），精准捕捉导致问题的场景。测试包含完整的溯源信息，可追踪至原始 QA 报告。

### 示例

```
You:   /qa https://staging.myapp.com

Claude: [Explores 12 pages, fills 3 forms, tests 2 flows]

        QA Report: staging.myapp.com — Health Score: 72/100

        Top 3 Issues:
        1. CRITICAL: Checkout form submits with empty required fields
        2. HIGH: Mobile nav menu doesn't close after selecting an item
        3. MEDIUM: Dashboard chart overlaps sidebar below 1024px

        [Full report with screenshots saved to .gstack/qa-reports/]
```

**测试需要认证的页面：**先使用 `/setup-browser-cookies` 导入你的真实浏览器会话，然后 `/qa` 就能测试需要登录的页面了。

---

## `/setup-browser-cookies`

这是我的**会话管理模式**。

在 `/qa` 或 `/browse` 测试需要认证的页面之前，它们需要 cookie。与其每次都通过无头浏览器（headless browser）手动登录，`/setup-browser-cookies` 能直接从你日常使用的浏览器导入真实会话。

它会自动检测已安装的 Chromium 内核浏览器（Comet、Chrome、Arc、Brave、Edge），通过 macOS 钥匙串解密 cookie，并将其加载到 Playwright 会话中。交互式选择界面让你精确选择要导入哪些域名——cookie 值绝不会被显示。

```
You:   /setup-browser-cookies

Claude: Cookie picker opened — select the domains you want to import
        in your browser, then tell me when you're done.

        [You pick github.com, myapp.com in the browser UI]

You:    done

Claude: Imported 2 domains (47 cookies). Session is ready.
```

或者跳过 UI，直接指定：

```
You:   /setup-browser-cookies github.com

Claude: Imported 12 cookies for github.com from Comet.
```

---

## `/retro`

这是我的**工程经理模式**。

每周结束时，我想知道实际发生了什么。不靠感觉——要数据。`/retro` 分析提交历史、工作模式和发布速度，撰写一份坦率的复盘报告。

它具备团队感知能力。识别出执行命令的人后，对你个人的工作投入最多笔墨，然后逐一拆解每位贡献者的表现，给出具体的表扬和成长建议。它计算提交数、代码行数、测试比例、PR 大小、修复率等指标。它能从提交时间戳中识别编码会话，找到热点文件，追踪连续发布天数，并标识本周最大的交付成果。

它还跟踪测试健康度：测试文件总数、本期新增测试、回归测试提交数和趋势变化。如果测试比例低于 20%，会将其标记为改进方向。

### 示例

```
You:   /retro

Claude: Week of Mar 1: 47 commits (3 contributors), 3.2k LOC, 38% tests, 12 PRs, peak: 10pm | Streak: 47d

        ## Your Week
        32 commits, +2.4k LOC, 41% tests. Peak hours: 9-11pm.
        Biggest ship: cookie import system (browser decryption + picker UI).
        What you did well: shipped a complete feature with encryption, UI, and
        18 unit tests in one focused push...

        ## Team Breakdown

        ### Alice
        12 commits focused on app/services/. Every PR under 200 LOC — disciplined.
        Opportunity: test ratio at 12% — worth investing before payment gets more complex.

        ### Bob
        3 commits — fixed the N+1 query on dashboard. Small but high-impact.
        Opportunity: only 1 active day this week — check if blocked on anything.

        [Top 3 team wins, 3 things to improve, 3 habits for next week]
```

它会将 JSON 快照保存到 `.context/retros/`，以便下次运行时展示趋势变化。

---

## `/document-release`

这是我的**技术写作模式**。

在 `/ship` 创建 PR 之后、合并之前，`/document-release` 会读取项目中每一个文档文件，并与 diff 交叉比对。它更新文件路径、命令列表、项目结构树，以及所有已过时的内容。有风险或涉及主观判断的改动会作为问题呈报——其余的自动处理。

```
You:   /document-release

Claude: Analyzing 21 files changed across 3 commits. Found 8 documentation files.

        README.md: updated skill count from 9 to 10, added new skill to table
        CLAUDE.md: added new directory to project structure
        CONTRIBUTING.md: current — no changes needed
        TODOS.md: marked 2 items complete, added 1 new item

        All docs updated and committed. PR body updated with doc diff.
```

它还会润色 CHANGELOG 的措辞（但绝不覆盖已有条目），清理已完成的 TODO，检查跨文档一致性，并仅在适当时询问是否需要更新版本号（VERSION）。

---

## Greptile 集成

[Greptile](https://greptile.com)（Greptile，YC 孵化的 PR 自动审查服务）是一家 YC（Y Combinator，硅谷知名创业孵化器）公司，能自动审查你的 PR。它捕捉的是真正的 bug——竞态条件、安全问题、那些能通过 CI 却在生产环境中爆炸的东西。它不止一次帮了我大忙。我真心喜欢这个团队。

### 配置

在 [greptile.com](https://greptile.com) 上为你的 GitHub 仓库安装 Greptile——大约 30 秒就能搞定。一旦它开始审查你的 PR，gstack（gstack，作者自建的 AI 编码代理系统框架）会自动获取它的评论。无需额外配置。

### 工作原理

任何自动审查工具的核心问题都是分诊。Greptile 很出色，但并非每条评论都是真问题。有些是误报（false positive），有些标记的是你三个提交之前就已经修复的东西。如果没有分诊层，评论会越积越多，你最终开始无视它们——这就完全背离了初衷。

gstack 解决了这个问题。`/review` 和 `/ship` 现在具备 Greptile 感知能力。它们会读取 Greptile 的评论，对每一条进行分类，并采取相应行动：

- **有效问题**会被纳入关键发现，在发布前修复
- **已修复的问题**会自动回复，确认已捕获
- **误报**会被反驳——你确认后，系统会发出回复解释为何判定有误

最终形成双层审查：Greptile 在 PR 上异步捕捉问题，然后 `/review` 和 `/ship` 在常规工作流中对这些发现进行分诊。不会有任何遗漏。

### 从历史中学习

你确认过的每一个误报都会被保存到 `~/.gstack/greptile-history.md`。后续运行会自动跳过你的代码库中已知的误报模式。`/retro` 还会随时间追踪 Greptile 的命中率——让你直观看到信噪比是否在改善。

### 示例

```
You:   /ship

Claude: [syncs main, runs tests, pre-landing review...]

        Greptile found 3 comments on this PR:

        [VALID] app/services/payment_service.rb:47 — Race condition:
        concurrent charges can double-debit. Recommend DB-level advisory
        lock around the charge block.

        [ALREADY FIXED] app/models/user.rb:12 — Missing null check
        on email before downcase.
        → Already fixed in commit abc1234. Auto-replying.

        [FALSE POSITIVE] lib/auth.rb:88 — "Token comparison should
        use constant-time comparison." We already use
        ActiveSupport::SecurityUtils.secure_compare here.

        Fixing the race condition in payment_service.rb...

        The auth token comment is a false positive.
        Options: A) Reply to Greptile explaining  B) Fix anyway  C) Ignore

You:    A

Claude: Replied to Greptile. All tests pass.
        PR: github.com/you/app/pull/42
```

三条 Greptile 评论。一个真正的修复。一个自动确认。一个误报被反驳并回复。额外耗时：大约 30 秒。
