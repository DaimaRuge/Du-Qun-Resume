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
- **下午 15:00**: 企业官网搜索

---

*最后更新: 2026-02-13*
