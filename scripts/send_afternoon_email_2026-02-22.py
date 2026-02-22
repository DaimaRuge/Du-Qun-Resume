#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
发送每日猎头任务邮件（下午场）- 2026-02-22
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# SMTP配置
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
SENDER_PASSWORD = "kgcokoehjimwlvcv"
RECIPIENT_EMAIL = "broadbtinp@gmail.com"

def send_email():
    """发送下午场邮件"""
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = f"🎯 每日猎头任务汇总 - 2026-02-22（下午场）"
    
    # 邮件内容
    body = """
您好！

这是2026年2月22日下午场的猎头任务执行报告。

========================================
📊 今日下午场任务执行情况
========================================

**执行时间**: 2026-02-22 14:00:13 (上海时间)

**新增搜索链接**: 5个
- LinkedIn: AI产品总监
- 猎聘: AI产品总监
- BOSS直聘: AI产品总监
- 前程无忧: AI产品总监
- 拉勾网: AI产品总监

========================================
🔗 下午场搜索链接
========================================

1. [LinkedIn] AI产品总监
   https://www.linkedin.com/jobs/search/?keywords=AI产品总监&location=China

2. [猎聘] AI产品总监
   https://www.liepin.com/zhaopin/?key=AI产品总监

3. [BOSS直聘] AI产品总监
   https://www.zhipin.com/web/geek/job?query=AI产品总监

4. [前程无忧] AI产品总监
   https://search.51job.com/list/000000,000000,0000,00,9,99,AI产品总监,2,1.html

5. [拉勾网] AI产品总监
   https://www.lagou.com/wn/zhaopin?kd=AI产品总监

========================================
📈 今日完整汇总（上午+下午）
========================================

**上午场**: 25个链接
**下午场**: 5个新增链接
**总计**: 30个搜索链接，覆盖5个平台

**目标职位**: AI产品总监、智能家居负责人、AIoT战略

========================================
💡 执行建议
========================================

1. 优先查看LinkedIn的国际化公司职位
2. 猎聘关注中高端职位机会
3. BOSS直聘快速响应率较高
4. 关注目标公司：华为、小米、字节跳动、涂鸦、绿米等

========================================
📁 相关资源
========================================

- 简历仓库: https://github.com/DaimaRuge/Du-Qun-Resume
- 飞书文档: 稍后创建

如有任何问题，请随时联系！

祝好！
AI猎头助手
2026-02-22 14:00
"""
    
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # 发送邮件
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("✅ 邮件发送成功！")
        print(f"   收件人: {RECIPIENT_EMAIL}")
        print(f"   主题: {msg['Subject']}")
        return True
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
        return False

if __name__ == "__main__":
    send_email()
