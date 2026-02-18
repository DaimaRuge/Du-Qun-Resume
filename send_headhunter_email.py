#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
猎头任务报告 - 邮件发送脚本
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime

# ============ SMTP 配置 ============
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
APP_PASSWORD = "kgcokoehjimwlvcv"

RECEIVERS = ["broadbtinp@gmail.com"]

# ============ 邮件内容 ============
today = datetime.now().strftime("%Y-%m-%d")
EMAIL_SUBJECT = f"🎯 AI猎头任务报告 - {today}"

EMAIL_BODY = f"""你好！

这是 {today} 的AI猎头任务执行报告。

📋 今日搜索任务：
- 搜索链接：25个
- 覆盖平台：LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网
- 目标职位：AI产品总监、智能家居负责人、AIoT战略

🔍 搜索关键词：
1. AI产品总监 / AI Product Director
2. 智能家居负责人 / Smart Home Lead  
3. AIoT战略负责人

🎯 重点目标公司：
- 大厂：华为、小米、字节、阿里、腾讯、百度
- 智能家居：海尔、美的、格力、涂鸦、绿米
- 机器人：科沃斯、石头科技、追觅、云鲸
- 外企：Bosch、Siemens、Samsung、LG

📊 执行建议：
1. 上午10:00-11:00：搜索并投递5-10个职位
2. 下午14:00-15:00：跟进投递状态，寻找新机会
3. 优先顺序：LinkedIn → 猎聘 → BOSS直聘 → 企业官网

📄 详细报告：
- GitHub: https://github.com/DaimaRuge/Du-Qun-Resume
- 飞书文档: 稍后更新

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
    print(f"🎯 猎头任务报告邮件发送 - {today}")
    print("=" * 60)
    print(f"发件人: {SENDER_EMAIL}")
    print(f"收件人: {', '.join(RECEIVERS)}")
    print(f"主题: {EMAIL_SUBJECT}")
    print("=" * 60)
    
    if send_email():
        print("\n✨ 完成！邮件已成功发送。")
    else:
        print("\n❌ 发送失败，请检查配置。")
