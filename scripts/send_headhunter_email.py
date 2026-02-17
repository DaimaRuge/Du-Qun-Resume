#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI猎头任务报告 - 邮件发送脚本
发件人: qun.xitang.du@gmail.com
收件人: broadbtinp@gmail.com
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

# 收件人
RECEIVER = "broadbtinp@gmail.com"

# ============ 报告文件路径 ============
REPORT_FILE = "/root/.openclaw/workspace/Headhunter_Reports/headhunter_report_2026-02-17.md"


def read_report():
    """读取报告内容"""
    try:
        with open(REPORT_FILE, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ 读取报告失败: {str(e)}")
        return None


def send_email(report_content):
    """发送邮件"""
    try:
        today = datetime.now().strftime("%Y-%m-%d")
        
        # 创建邮件对象
        msg = MIMEMultipart()
        msg['From'] = formataddr(("AI Headhunter Assistant", SENDER_EMAIL))
        msg['To'] = RECEIVER
        msg['Subject'] = f"🎯 每日猎头任务报告 - {today}"
        
        # 邮件正文
        email_body = f"""你好！

这是 {today} 的AI猎头任务报告，包含以下内容：

📋 搜索链接清单（25个）
   - LinkedIn: 5个搜索链接
   - 猎聘: 5个搜索链接
   - BOSS直聘: 5个搜索链接
   - 前程无忧: 5个搜索链接
   - 拉勾网: 5个搜索链接

🎯 目标公司清单
   - 大厂: 华为、小米、字节、阿里等
   - 智能家居: 海尔、美的、格力等
   - 外企: Google、Amazon、Tesla等

📝 执行建议
   - 优先顺序: LinkedIn → 猎聘 → BOSS直聘
   - 每日任务: 上午10点和下午2点
   - 投递策略: 突出AI产品经验

完整报告内容见下方。

祝求职顺利！🚀

---
AI Headhunter Assistant
{today}

{'='*60}

"""
        
        msg.attach(MIMEText(email_body + report_content, 'plain', 'utf-8'))
        
        print(f"📧 正在连接 SMTP 服务器: {SMTP_SERVER}:{SMTP_PORT}")
        
        # 连接服务器并发送
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        
        print(f"✅ 登录成功")
        print(f"📤 正在发送邮件给: {RECEIVER}")
        
        server.sendmail(SENDER_EMAIL, [RECEIVER], msg.as_string())
        
        print(f"✅ 邮件发送成功！")
        server.quit()
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("📧 AI猎头任务报告 - 邮件发送")
    print("=" * 60)
    
    # 读取报告
    report_content = read_report()
    if not report_content:
        sys.exit(1)
    
    print(f"✅ 报告读取成功 ({len(report_content)} 字符)")
    print(f"发件人: {SENDER_EMAIL}")
    print(f"收件人: {RECEIVER}")
    print("=" * 60)
    
    if send_email(report_content):
        print("\n✨ 完成！邮件已成功发送。")
        sys.exit(0)
    else:
        print("\n❌ 发送失败，请检查配置。")
        sys.exit(1)
