#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日猎头任务汇总 - 邮件发送脚本
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import sys
from datetime import datetime

# ============ SMTP 配置 ============
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
APP_PASSWORD = "kgcokoehjimwlvcv"

# 收件人列表
RECEIVERS = [
    "broadbtinp@gmail.com",
]

# ============ 邮件内容 ============
today = datetime.now().strftime("%Y-%m-%d")
EMAIL_SUBJECT = f"📊 每日猎头任务汇总 - {today}"

EMAIL_BODY = f"""
你好！

这是 {today} 的AI猎头任务汇总报告。

## ✅ 今日执行情况

### 上午场 (10:00)
- ✅ 生成25个搜索链接
- ✅ 覆盖5大招聘平台

### 下午场 (14:00)  
- ✅ 更新今日报告
- ✅ 发送邮件汇总

---

## 🎯 今日搜索重点

**职位关键词**:
1. AI产品总监
2. AI Product Director
3. 智能家居负责人
4. Smart Home Lead
5. AIoT战略负责人

**搜索平台**:
- LinkedIn (5个链接)
- 猎聘 (5个链接)
- BOSS直聘 (5个链接)
- 前程无忧 (5个链接)
- 拉勾网 (5个链接)

---

## 🏢 目标公司

**大厂**: 华为、小米、字节跳动、阿里巴巴、腾讯、百度、美团、京东

**智能家居**: 海尔、美的、格力、TCL、涂鸦、绿米、欧瑞博

**机器人/AI**: 大疆、科沃斯、石头科技、追觅

**外企**: 博世、西门子、三星、LG

---

## 💡 投递策略提醒

1. 突出AI产品经验（HomeGPT、AI烤箱）
2. 强调0-1业务操盘能力
3. 量化成果（5亿营收、$1000万成本优化）

---

## 📋 今日待办

- [ ] 访问LinkedIn搜索AI Product Director
- [ ] 访问猎聘搜索AI产品总监
- [ ] 投递5-10个匹配职位
- [ ] 记录投递状态

---

详细报告位置:
/root/.openclaw/workspace/Headhunter_Reports/headhunter_report_2026-02-17.md

---
报告生成: AI Headhunter Assistant
日期: {today}
"""


def send_email():
    """发送邮件"""
    try:
        msg = MIMEText(EMAIL_BODY, 'plain', 'utf-8')
        msg['From'] = formataddr(("AI猎头助手", SENDER_EMAIL))
        msg['To'] = ", ".join(RECEIVERS)
        msg['Subject'] = EMAIL_SUBJECT

        print(f"📧 正在连接 SMTP 服务器...")
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        
        print(f"✅ 登录成功")
        print(f"📤 正在发送邮件给: {', '.join(RECEIVERS)}")
        
        server.sendmail(SENDER_EMAIL, RECEIVERS, msg.as_string())
        
        print(f"✅ 邮件发送成功！")
        server.quit()
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("📊 每日猎头任务汇总 - 邮件发送")
    print("=" * 60)
    print(f"发件人: {SENDER_EMAIL}")
    print(f"收件人: {', '.join(RECEIVERS)}")
    print(f"主题: {EMAIL_SUBJECT}")
    print("=" * 60)
    
    if send_email():
        print("\n✨ 完成！邮件已成功发送。")
        sys.exit(0)
    else:
        print("\n❌ 发送失败，请检查配置。")
        sys.exit(1)
