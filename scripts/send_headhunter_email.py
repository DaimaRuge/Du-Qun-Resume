#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日猎头任务进展报告 - 邮件发送脚本
发件人: qun.xitang.du@gmail.com
收件人: broadbtinp@gmail.com, dulie@foxmail.com
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime
import sys

# ============ SMTP 配置 ============
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
APP_PASSWORD = "kgcokoehjimwlvcv"  # App Password

# 收件人列表
RECEIVERS = [
    "broadbtinp@gmail.com",
    "dulie@foxmail.com"
]

# ============ 邮件内容 ============
today = datetime.now().strftime("%Y-%m-%d")
EMAIL_SUBJECT = f"📊 每日猎头任务进展报告 - {today}"

EMAIL_BODY = f"""你好！

这是今日（{today}）的AI猎头任务进展报告。

## ✅ 今日任务完成情况

### 上午任务 (10:00)
- ✅ 生成25个搜索链接
- ✅ 覆盖5大招聘平台（LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网）
- ✅ 聚焦10个核心职位关键词

### 下午任务 (14:00)
- ✅ 追加5个AI产品总监相关搜索
- ✅ 更新今日搜索报告

---

## 🎯 今日搜索重点

### 核心职位
- AI产品总监 / AI Product Director
- 智能家居负责人 / Smart Home Lead
- AIoT战略负责人
- 产品总监 / Product Director
- 智能硬件产品

### 目标公司
- 大厂: 华为、小米、字节、阿里、腾讯、百度、美团、京东
- 智能家居: 海尔、美的、格力、TCL、涂鸦、绿米、欧瑞博
- 机器人/AI: 大疆、优必选、科沃斯、石头科技、追觅
- 外企: 博世、西门子、三星、LG、松下

---

## 📋 快速搜索链接

### LinkedIn (国际化公司)
https://www.linkedin.com/jobs/search/?keywords=AI产品总监&location=China

### 猎聘 (中高端职位)
https://www.liepin.com/zhaopin/?key=AI产品总监

### BOSS直聘 (快速响应)
https://www.zhipin.com/web/geek/job?query=AI产品总监

---

## 📝 明日行动建议

1. 访问上述链接投递5-10个职位
2. 重点跟进华为、小米、涂鸦、博世等目标公司
3. 突出AI产品经验（HomeGPT、AI烤箱）
4. 强调量化成果（5亿营收、$1000万成本优化）

---

## 📂 相关文档

- 优化简历 (中文): https://feishu.cn/docx/PAU2dqKOgo5gPNxaenlch6STn3e
- 优化简历 (英文): https://feishu.cn/docx/H2l0dpZPhomdURx53Xic1uMXn7f
- GitHub仓库: https://github.com/DaimaRuge/Du-Qun-Resume

---

**报告生成**: AI Headhunter Assistant
**下次执行**: 明日 10:00
"""


def send_email():
    """发送邮件"""
    try:
        # 创建邮件对象
        msg = MIMEText(EMAIL_BODY, 'plain', 'utf-8')
        msg['From'] = formataddr(("杜群", SENDER_EMAIL))
        msg['To'] = ", ".join(RECEIVERS)
        msg['Subject'] = EMAIL_SUBJECT

        print(f"📧 正在连接 SMTP 服务器: {SMTP_SERVER}:{SMTP_PORT}")
        
        # 连接服务器并发送
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # 启用TLS加密
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
    print("📊 每日猎头任务进展报告 - 邮件发送")
    print("=" * 60)
    print(f"发件人: {SENDER_EMAIL}")
    print(f"收件人: {', '.join(RECEIVERS)}")
    print(f"主题: {EMAIL_SUBJECT}")
    print("=" * 60)
    
    if send_email():
        print("\n✨ 完成！进展报告已发送。")
        sys.exit(0)
    else:
        print("\n❌ 发送失败，请检查配置。")
        sys.exit(1)
