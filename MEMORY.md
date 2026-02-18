# MEMORY.md - 工作流程与偏好记录

> 此文件记录用户的常用工作流程和偏好设置。

---

## 📧 邮件服务配置

**状态**: ✅ 已配置 (Gmail SMTP)
**SMTP服务器**: smtp.gmail.com
**端口**: 587 (TLS)
**应用密码**: kgcokoehjimwlvcv

**发件人**: qun.xitang.du@gmail.com

**收件人列表**:
- broadbtinp@gmail.com
- dulie@foxmail.com

**工具**: Python smtplib 脚本
**脚本位置**: `/root/.openclaw/workspace/send_email.py`

**操作**:
- [x] 2026-02-10: 配置SMTP并发送VibeVoice项目分析报告
- [x] 2026-02-12: 发送 Skill Marketplace 商业计划书

---

## 📄 飞书文档操作

**已完成操作**:
1. ✅ 创建飞书文档 "VibeVoice 项目完整分析报告"
   - 链接: https://feishu.cn/docx/SU4fdlcbJofon3xpSbZcsWaTnpb
   - 时间: 2026-02-10
2. ✅ 创建飞书文档 "Skill Marketplace 商业计划书"
   - 链接: https://feishu.cn/docx/H3hkdM9FToaKh4xEuEYcOtp2nVf
   - 时间: 2026-02-12

**工作流程**:
1. 生成Markdown报告
2. 使用feishu_doc创建飞书文档
3. 发送飞书消息通知

---

## 📝 简历管理

**简历版本**:
- **V3.5 (2025-12-16)**: 原始版本，包含最新工作经历
- **V2.0 (2026-02-12)**: AI增强版，添加AI技能和项目经验
- **V3.5 + AI (2026-02-13)**: 融合版本，基于V3.5内容 + AI增强

**文件位置**:
- 中文版: `/root/.openclaw/workspace/Du_Qun_Resume_CN_V3.5_AI.md` (6KB)
- 英文版: `/root/.openclaw/workspace/Du_Qun_Resume_EN_V3.5_AI.md` (10.7KB)

**GitHub仓库**:
- 仓库地址: https://github.com/DaimaRuge/Du-Qun-Resume
- 包含文件: 中英文简历 + Skill Marketplace商业计划书

---

## 🎯 标准工作流程

### 文档分享流程

**当用户要求分享文档时**:
1. ✅ 生成详细的Markdown报告
2. ✅ 创建飞书文档 (feishu_doc create)
3. ✅ 通过飞书消息发送链接通知用户

### 邮件发送流程

**当用户要求发送邮件时**:
1. ✅ 使用Python smtplib发送
2. ✅ 附加Markdown文档内容
3. ✅ 多收件人支持

---

## 📋 用户偏好

- **文档格式**: 详细Markdown报告
- **分享方式**: 优先使用飞书文档
- **邮件服务**: 期望使用SMTP配置
- **工作流程**: 标准化、自动化

---

## 🧘 吾日三省吾身 - 每日工作流程

**建立日期**: 2026-02-10

**核心要求**: 每天执行三件事

### 第一省：今天进化了没有？

**任务**: 寻找并安装新技能 (1-3个)

**关注领域**:
- Claude Hub技能
- awesome opencloud开源项目
- 记忆、搜索、文档处理、理解相关技能

**执行频率**: 每天

### 第二省：今天学习了吗？

**任务**: 反思学习成果与不足

**关注点**:
- 今天完成了哪些学习任务？
- 有什么进步？
- 明天需要改进什么？

**执行频率**: 每天

### 第三省：找IoT/AI/机器人项目了吗？

**任务**: 寻找相关开源项目 (1-3个)

**关注领域**:
- IoT智能家居
- AI大模型
- Agent
- ASR/TTS语音技术
- 机器人/硬件

**执行频率**: 每天

### 输出文档

**位置**: `/root/.openclaw/workspace/Daily_Self_Reflections/YYYY-MM-DD_三省吾身报告.md`

**内容**:
- 推荐技能清单
- 学习总结
- 项目调研报告
- 明日行动计划

### 2026-02-10 完成情况

✅ **进化**: 找到3个推荐技能 (Pipecat, ChatGPT-on-WeChat, Home Assistant)
✅ **学习**: 完成VibeVoice深度分析，建立邮件工作流程
✅ **项目调研**: 找到20+相关开源项目

---

## 📊 每日健康检查系统

### 日报生成
- **脚本**: `/root/.openclaw/workspace/scripts/daily_health_check.py`
- **输出**: `/root/.openclaw/workspace/Daily_Reports/daily_report_YYYY-MM-DD.md`
- **时间**: 每晚10点自动执行 (cron)

### 检查内容
- [x] CPU使用率和负载
- [x] 内存使用情况
- [x] 磁盘空间占用
- [x] OpenClaw版本和状态
- [ ] Token消耗统计 (待完善)
- [ ] 对话数量统计 (待完善)

### 文件位置
- 日报目录: `/root/.openclaw/workspace/Daily_Reports/`
- 天气状态: `/root/.openclaw/workspace/Daily_Reports/weather_status.json`

---

## 🌤️ 天气监控

### 监控城市
- 上海 (Shanghai)
- 福州 (Fuzhou)
- 合肥 (Hefei)

### 监控规则
- 每天检查天气预报
- 如果明天任一城市下雨，立即提醒用户
- 持续提醒直到用户确认

### 天气脚本
- **位置**: `/root/.openclaw/workspace/scripts/weather_check.py`
- **状态**: 待配置API Key

---

## 🎯 吾日三省吾身流程

### 每日任务 (每晚10-11点)

1. **一省：今天进化了没有？**
   - 检查Claude Hub/开源项目找新技能
   - 安装1-3个提升能力的技能
   - 领域: 记忆、搜索、文档处理、AI理解

2. **二省：今天学习了吗？**
   - 阅读技术文档/论文
   - 分析项目代码
   - 学习新技术栈

3. **三省：找IoT/AI/机器人相关项目**
   - 搜索开源项目
   - 评估实用性
   - 给出brief和推荐

### 输出
- **日报**: `/root/.openclaw/workspace/Daily_Reports/`
- **三省报告**: `/root/.openclaw/workspace/Daily_Self_Reflections/`

---

## 🔧 OpenClaw 升级命令

**升级命令**: `npm i -g openclaw@latest`

**说明**: 用户指定的升级命令，用于将OpenClaw更新到最新版本

**执行时间**: 2026-02-10
**升级结果**: 2026.2.6-3 → 2026.2.9 ✅

---

## 💾 配置文件备份

**备份命令**:
```bash
mkdir -p /root/.openclaw/workspace/backups/YYYY-MM-DD
cp ~/.openclaw/openclaw.json /root/.openclaw/workspace/backups/YYYY-MM-DD/
cp -r ~/.openclaw/credentials/ /root/.openclaw/workspace/backups/YYYY-MM-DD/
tar -czvf /root/.openclaw/workspace/backups/YYYY-MM-DD/workspace_backup.tar.gz ~/.openclaw/workspace/ --exclude='node_modules' --exclude='.git'
```

**备份位置**: `/root/.openclaw/workspace/backups/`

**首次备份**: 2026-02-10
- openclaw.json (4.1KB)
- credentials/ (180B)
- workspace_backup.tar.gz (530MB)

---

## 📁 重要目录结构

```
~/.openclaw/
├── openclaw.json          (主配置文件)
├── credentials/           (凭证目录)
└── workspace/
    ├── backups/           (备份目录)
    │   └── YYYY-MM-DD/    (按日期备份)
    ├── Daily_Reports/     (每日健康报告)
    ├── Daily_Self_Reflections/ (三省吾身报告)
    ├── scripts/           (脚本目录)
    └── memory/            (每日笔记)
```

---

---

## 🎯 求职助手任务

**创建日期**: 2026-02-13

### 任务目标
- 每日搜索产品总监/AIoT产品经理职位
- 目标平台：LinkedIn、猎聘、企业官网
- 每天至少2次搜索
- 结果通过邮件、GitHub、飞书汇报

### 搜索关键词
- 产品总监
- 产品管理
- AIoT 产品经理
- 智能家居产品
- 战略产品经理

### 目标公司

**国内企业**:
- **智能家居**: 小米、华为、海尔、美的、格力
- **AIoT平台**: 涂鸦、绿米、欧瑞博
- **汽车电子**: 科博达、德赛西威、华阳集团
- **酒店科技**: 华住、携程、美团
- **机器人**: 科沃斯、石头科技、追觅

**外资企业**:
- **智能家居/IoT**: Google Nest, Amazon Alexa, Apple HomeKit, Samsung SmartThings, Philips Hue, Bosch, Siemens, Electrolux, Dyson
- **汽车电子**: Tesla, Bosch, Continental, Valeo, Denso, Aptiv
- **科技/互联网**: Microsoft, Google, Apple, Amazon, Meta, Nvidia, Intel, Qualcomm
- **酒店/商业地产**: Marriott, Hilton, IHG, Accor

### 汇报机制
- **每日**: 邮件发送搜索结果到 broadbtinp@gmail.com
- **GitHub**: 提交每日搜索报告
- **飞书**: 创建求职机会汇总文档

### 定时任务
- **上午 10:00**: LinkedIn + 猎聘搜索
- **下午 14:00**: 猎聘 + 企业官网搜索

---

## 📋 2026-02-13 工作完成记录

### ✅ 简历优化任务

**完成时间**: 2026-02-13 06:15

**优化内容**:
1. ✅ 生成 V4.0 优化版简历（中文+英文）
2. ✅ 突出AI/Agent实战经验
3. ✅ 强化量化成果（5亿营收、$1000万成本优化）
4. ✅ 提升可扫描性（核心价值主张、顶级成就表格）
5. ✅ 跨行业适配（智能环境、商业地产）

**文件位置**:
- 中文版: `/root/.openclaw/workspace/Du_Qun_Resume_CN_V4.0_Optimized.md`
- 英文版: `/root/.openclaw/workspace/Du_Qun_Resume_EN_V4.0_Optimized.md`

**飞书文档**:
- 中文版: https://feishu.cn/docx/PAU2dqKOgo5gPNxaenlch6STn3e
- 英文版: https://feishu.cn/docx/H2l0dpZPhomdURx53Xic1uMXn7f

**GitHub**:
- 仓库: https://github.com/DaimaRuge/Du-Qun-Resume
- 提交: `feat: Add optimized resume V4.0 - AI Product Director focus (CN + EN)`

**邮件通知**:
- ✅ 已发送至 broadbtinp@gmail.com

### ✅ 猎头任务设置

**完成时间**: 2026-02-13 06:20

**Cron Job设置**:
1. ✅ 每日猎头任务-上午 (10:00 上海时区)
   - Job ID: 905b285f-fd28-44e5-a704-d1e7a45e950a
2. ✅ 每日猎头任务-下午 (14:00 上海时区)
   - Job ID: 69ab8668-0e31-445d-8183-742ec91a670c

**任务内容**:
- 搜索LinkedIn、猎聘、BOSS直聘等平台
- 寻找AI产品总监、智能家居负责人、AIoT战略等职位
- 生成搜索报告并邮件/飞书/GitHub汇报

**脚本位置**:
- `/root/.openclaw/workspace/scripts/headhunter_task.py`

**报告位置**:
- `/root/.openclaw/workspace/Headhunter_Reports/headhunter_report_YYYY-MM-DD.md`

---

---

## 🏠 智能家居设备控制智能体项目

**项目代号**: SmartHome-Agent
**启动日期**: 2026-02-13
**状态**: 立项与规划阶段

### 项目概述
- AI驱动的智能家居设备控制系统
- 支持多品牌、多协议设备
- 自然语言控制 + 场景自动化

### 核心功能
1. **AI智能体**: NLU、意图识别、多轮对话
2. **设备控制**: 多协议、多品牌接入
3. **场景引擎**: 预设场景、自定义场景、触发器

### 技术栈
- AI: OpenClaw Agent + GLM-5
- 后端: Node.js/Python
- 协议: MQTT, HTTP, WebSocket
- 数据库: PostgreSQL + Redis

### 项目文件
- 立项文档: `/projects/smarthome-agent/PROJECT_CHARTER.md`
- 技术方案: `/projects/smarthome-agent/TECHNICAL_DESIGN.md`
- 任务清单: `/projects/smarthome-agent/TODO.md`
- GitHub: https://github.com/DaimaRuge/Du-Qun-Resume

### 里程碑
- M1: 需求确认 (2026-02-20)
- M2: 设计完成 (2026-03-06)
- M3: Alpha版本 (2026-04-10)
- M4: Beta版本 (2026-04-24)
- M5: 正式发布 (2026-05-08)

---

## 📋 2026-02-17 猎头任务执行记录

### ✅ 下午场 (14:00)
1. ✅ 运行 headhunter_task.py 脚本
2. ✅ 更新今日报告
3. ✅ 发送邮件汇总至 broadbtinp@gmail.com
4. ✅ 创建飞书文档: https://feishu.cn/docx/W7y6dMXCgoEeEhxPZhscJusAnWg
5. ✅ GitHub同步: commit 8f45333

### 今日搜索统计
- 搜索链接: 25个
- 覆盖平台: 5个 (LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网)
- 目标职位: AI产品总监、智能家居负责人、AIoT战略

---

## 📋 2026-02-18 猎头任务执行记录

### ✅ 上午场 (10:00)
1. ✅ 运行 headhunter_task.py 脚本生成搜索链接
2. ✅ 读取报告内容 (25个链接)
3. ✅ 发送邮件汇总至 broadbtinp@gmail.com
4. ✅ 创建飞书文档: https://feishu.cn/docx/IlIidCNNtowaq6xbWgzcrF1AnZ4
5. ✅ GitHub同步: commit ef49407

### 今日搜索统计
- 搜索链接: 25个
- 覆盖平台: 5个 (LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网)
- 目标职位: AI产品总监、智能家居负责人、AIoT战略
- 执行时间: 2026-02-18 10:00:07 (上海时间)

### ✅ 下午场 (14:00)
1. ✅ 运行 headhunter_task.py 脚本生成新增搜索链接
2. ✅ 发送邮件汇总至 broadbtinp@gmail.com (包含上午+下午场)
3. ✅ 创建飞书文档（下午场）: https://feishu.cn/docx/TyMid5M05oJFWIx8xUzc92IIn4g
4. 🔄 GitHub同步: 待提交

### 下午场搜索统计
- 新增链接: 5个
- 执行时间: 2026-02-18 14:00:23 (上海时间)
- 邮件主题: 🎯 每日猎头任务汇总 - 2026-02-18（下午场）

### 📊 今日完整汇总
- **上午场**: 25个链接 + 邮件 + 飞书 + GitHub (commit ef49407)
- **下午场**: 5个新增链接 + 邮件 + 飞书
- **总计**: 30个搜索链接，覆盖5个平台

---

*最后更新: 2026-02-18 14:05*
