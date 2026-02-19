#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日猎头任务报告 - 邮件发送脚本
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import sys
from datetime import datetime

# ============ SMTP 配置 ============
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
APP_PASSWORD = "kgcokoehjimwlvcv"

# 收件人
RECEIVERS = ["broadbtinp@gmail.com"]

def send_email(report_file):
    """发送猎头任务报告邮件"""
    try:
        # 读取报告内容
        with open(report_file, 'r', encoding='utf-8') as f:
            report_content = f.read()
        
        # 提取日期
        today = datetime.now().strftime('%Y-%m-%d')
        
        # 邮件主题
        subject = f"🎯 每日猎头任务汇总 - {today}"
        
        # 邮件内容
        body = f"""你好！

这是今日的AI猎头任务搜索结果汇总：

{report_content}

---
报告生成: AI Headhunter Assistant
时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        # 创建邮件
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = formataddr(("AI猎头助手", SENDER_EMAIL))
        msg['To'] = ", ".join(RECEIVERS)
        msg['Subject'] = subject
        
        # 发送邮件
        print(f"📧 正在连接 SMTP 服务器...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        
        print(f"✅ 登录成功")
        print(f"📤 正在发送邮件给: {', '.join(RECEIVERS)}")
        
        server.sendmail(SENDER_EMAIL, RECEIVERS, msg.as_string())
        server.quit()
        
        print(f"✅ 邮件发送成功！")
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 请提供报告文件路径")
        sys.exit(1)
    
    report_file = sys.argv[1]
    print("=" * 60)
    print("📧 每日猎头任务报告 - 邮件发送")
    print("=" * 60)
    
    if send_email(report_file):
        print("\n✨ 完成！邮件已成功发送。")
        sys.exit(0)
    else:
        print("\n❌ 发送失败")
        sys.exit(1)
