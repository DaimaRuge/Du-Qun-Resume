#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
猎头任务报告 - 邮件发送脚本
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import sys
import os
from datetime import datetime

# ============ SMTP 配置 ============
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
APP_PASSWORD = "kgcokoehjimwlvcv"

# 收件人
RECEIVERS = ["broadbtinp@gmail.com"]

# ============ 报告路径 ============
REPORT_DATE = datetime.now().strftime("%Y-%m-%d")
REPORT_PATH = f"/root/.openclaw/workspace/Headhunter_Reports/headhunter_report_{REPORT_DATE}.md"


def read_report():
    """读取今日报告"""
    try:
        with open(REPORT_PATH, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ 报告文件不存在: {REPORT_PATH}")
        return None


def send_email(report_content):
    """发送邮件"""
    try:
        msg = MIMEMultipart()
        msg['From'] = formataddr(("AI猎头助手", SENDER_EMAIL))
        msg['To'] = ", ".join(RECEIVERS)
        msg['Subject'] = f"🎯 猎头任务报告 - {REPORT_DATE}"

        # 邮件正文
        email_body = f"""你好！

这是今日 ({REPORT_DATE}) 的AI猎头任务报告，包含最新的职位搜索链接和目标公司清单。

报告内容：
- 25个职位搜索链接（LinkedIn、猎聘、BOSS直聘等）
- 重点目标公司清单
- 执行建议和策略

详细报告请见附件或查看下方内容。

---
{report_content[:3000]}

...（完整报告请查看飞书文档）
---

🤖 AI Headhunter Assistant
"""
        
        msg.attach(MIMEText(email_body, 'plain', 'utf-8'))

        print(f"📧 正在连接 SMTP 服务器: {SMTP_SERVER}:{SMTP_PORT}")
        
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
    print(f"📧 猎头任务报告邮件发送 - {REPORT_DATE}")
    print("=" * 60)
    
    # 读取报告
    report = read_report()
    if not report:
        sys.exit(1)
    
    # 发送邮件
    if send_email(report):
        print("\n✨ 完成！邮件已成功发送。")
        sys.exit(0)
    else:
        print("\n❌ 发送失败，请检查配置。")
        sys.exit(1)
