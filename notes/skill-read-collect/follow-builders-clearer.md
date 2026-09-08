# follow-builders 技能说明汇总

## 1. 功能

这个技能的核心用途，是把 AI 行业里一批“真正做事的 builders”近期公开表达的内容，整理成可定期接收的 digest。它关注的不是泛泛而谈的 influencer，而是研究者、创业者、产品负责人、工程负责人等实际在构建 AI 产品和公司的群体。

它主要解决三个问题：

- 帮用户持续追踪 AI builders 在 X 和 YouTube 播客中的最新观点与动作
- 把原始内容重组为更容易阅读的日报或周报摘要
- 按用户偏好，以终端、Telegram、邮件或 OpenClaw 当前聊天通道的方式交付

从使用体验上看，这不是一个“临时搜索一下 AI 新闻”的技能，而是一个带有配置、定时投递、首次 onboarding、后续可调整偏好的长期摘要助手。

它覆盖两类使用场景：

- 首次安装和配置后，按日或按周自动发送摘要
- 用户主动输入 /ai 时，立即执行一次手动 digest 生成

## 2. 用什么技术或能力实现

这个技能本质上是“中心化内容源 + 本地配置 + 脚本准备数据 + LLM 负责重组表达 + 多通道交付”的组合流程。

关键实现方式如下：

- 平台识别：先通过 which openclaw 判断当前运行环境是 OpenClaw 还是其他非持久 agent 环境。不同平台会直接影响投递方式和 cron 方案。
- 本地配置持久化：把用户偏好写入 ~/.follow-builders/config.json，包括语言、时区、频率、发送时间、投递方式等。
- 环境变量管理：只有在 Telegram 或 Email 投递时才需要 ~/.follow-builders/.env 中的密钥。内容抓取本身不依赖用户 API key。
- 数据准备脚本：通过 scripts/prepare-digest.js 统一准备输入数据。这个脚本负责拉取中心 feed、读取 prompts、拼出一个 JSON 输出，供后续摘要生成使用。
- LLM 重组能力：技能明确要求 agent 不直接联网抓网页，而是只基于 prepare-digest.js 输出的 JSON 做“remix”。也就是说，模型的职责是摘要、改写、翻译和编排，不是采集数据。
- Prompt 分层：摘要逻辑依赖多个 prompt 字段，包括 digest_intro、summarize_podcast、summarize_tweets 和 translate。它把“整体 framing”“推文摘要”“播客摘要”“中文翻译”拆成独立规则。
- 语言输出控制：支持英文、中文、双语三种模式。双语模式要求英文和中文按段交错输出，而不是先整篇英文再整篇中文。
- 交付脚本：若投递到 Telegram 或 Email，则使用 scripts/deliver.js 完成发送；若是 stdout，则直接在当前对话或终端输出。
- 定时调度：
  - OpenClaw 环境使用 openclaw cron add，并且必须显式指定 channel 和 target，不能偷懒用 --channel last
  - 非持久环境中，如果选择 Telegram 或 Email，则通过系统 crontab 做定时发送
  - 非持久环境且只做按需使用时，则不设 cron，只允许手动触发

这个技能还有几个实现上的硬约束：

- 内容来源由中心 feed 统一维护，用户不能直接增删 source
- 生成摘要时不能自行访问 x.com、搜索网页或调用额外 API
- 每条保留的内容都必须带原始 URL，没有 URL 就不能收录
- 职位信息要优先读 bio，不能凭模型猜测

这些约束说明，这个技能被设计成“数据获取确定化、表达生成可控化”的结构，目的是降低幻觉和信息漂移。

## 3. 我可以如何触发使用这个技能

这个技能的触发主要有三类。

第一类是首次开通或配置型请求。典型说法包括：

- 帮我配置 AI builders digest
- 给我开一个每天推送 AI builder 摘要的助手
- 我想每周收到一次 AI 行业 builders 更新
- 帮我把摘要改成中文
- 帮我把发送时间改成早上 8 点

这类请求会触发 onboarding 或 configuration handling。技能会询问频率、时间、时区、语言、投递方式，并写入配置文件。

第二类是手动运行摘要。最明确的触发方式是：

- /ai

除此之外，类似下面的表达也很可能落到同一套手动 digest 流程：

- 给我今天的 AI builders digest
- 拉一下最新的 builders 更新
- 现在生成一份 AI builder 摘要

第三类是配置修改与查询请求，例如：

- 改成 weekly digest
- 时区改成 America/New_York
- 改成双语输出
- 切换到 Telegram 发送
- 把摘要写短一点
- 展示我当前设置
- 我在跟谁

这些请求会分别触发 schedule、language、delivery、prompt 或 info request 相关逻辑。

## 补充理解

这个技能有几个很重要的边界，使用者最好提前知道：

- 它不是通用新闻搜索器，而是围绕预先维护好的 builder 和 podcast 来源做摘要。
- source list 由中心统一维护。如果用户要新增或删除关注对象，技能给出的标准处理是引导去仓库提 issue，而不是本地直接修改。
- 在 OpenClaw 中，这个技能最完整，因为它支持真正的定时、通道投递与校验。
- 在 Claude Code、Cursor 这类非持久环境里，如果要自动投递，只能依赖 Telegram 或 Email；否则就只能按需手动运行。
- 非持久环境下用系统 crontab 直连 prepare-digest.js 和 deliver.js 时，文档明确提醒这可能绕过 LLM remix，最终发送的内容质量会弱于手动 /ai 路径。
- 首次 onboarding 后，技能要求立刻发送一份 welcome digest，让用户马上看到结果，并根据反馈继续微调。

如果从技能设计角度看，follow-builders 不是单纯的“提示词模板”，而是一个已经产品化的工作流技能：它把来源采集、配置存储、内容整理、翻译、投递和后续偏好修改全都定义清楚了，适合作为长期订阅型 AI 信息服务的 agent 技能样板。
