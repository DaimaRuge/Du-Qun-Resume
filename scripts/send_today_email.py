#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# SMTP配置
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "qun.xitang.du@gmail.com"
SMTP_PASSWORD = "kgcokoehjimwlvcv"

# 收件人
TO_EMAIL = "broadbtinp@gmail.com"

# 获取当前日期
today_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 邮件内容
subject = f"🎯 每日猎头任务汇总 - {today_date}（下午场）"

body = f"""🎯 AI猎头任务 - 下午场汇总

日期: {today_date}
时间: {current_time} (UTC)

---

## 📊 今日进展统计

### 上午场 (10:00)
- 搜索链接: 25个
- 覆盖平台: LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网
- 目标职位: AI产品总监、智能家居负责人、AIoT战略

### 下午场 (14:00)
- 新增搜索链接: 5个
- 重点跟进: 上午投递状态检查
- 寻找新机会: 各平台最新职位

---

## 🎯 搜索链接清单

### 下午场新增链接

1. LinkedIn - AI产品总监
https://www.linkedin.com/jobs/search/?keywords=AI产品总监&location=China

2. 猎聘 - AI产品总监
https://www.liepin.com/zhaopin/?key=AI产品总监

3. BOSS直聘 - AI产品总监
https://www.zhipin.com/web/geek/job?query=AI产品总监

4. 前程无忧 - AI产品总监
https://search.51job.com/list/000000,000000,0000,00,9,99,AI产品总监,2,1.html

5. 拉勾网 - AI产品总监
https://www.lagou.com/wn/zhaopin?kd=AI产品总监

---

## 📝 执行建议

1. 检查上午投递的职位反馈
2. 访问下午场新增链接，寻找新机会
3. 重点跟进目标公司的职位发布
4. 更新投递记录表

---

## 🎯 目标公司

**重点方向**:
- 智能家居: 小米、华为、海尔、美的、涂鸦、绿米、欧瑞博
- AI/机器人: 科大讯飞、大疆、优必选、科沃斯、石头科技、追觅
- 互联网: 阿里、腾讯、字节、百度、美团、京东
- 外企: Google、Amazon、Bosch、Siemens、Samsung、LG

---

报告位置: /root/.openclaw/workspace/Headhunter_Reports/headhunter_report_{today_date}.md

---
AI Headhunter Assistant
"""

# 创建邮件
msg = MIMEMultipart()
msg['From'] = SMTP_USER
msg['To'] = TO_EMAIL
msg['Subject'] = subject

# 添加邮件正文
msg.attach(MIMEText(body, 'plain', 'utf-8'))

# 发送邮件
print("=" * 60)
print("📧 每日猎头任务汇总 - 邮件发送")
print("=" * 60)
print(f"发件人: {SMTP_USER}")
print(f"收件人: {TO_EMAIL}")
print(f"主题: {subject}")
print("=" * 60)

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(SMTP_USER, TO_EMAIL, msg.as_string())
    server.quit()
    print("✅ 邮件发送成功！")
except Exception as e:
    print(f"❌ 邮件发送失败: {e}")
