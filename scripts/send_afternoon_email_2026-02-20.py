#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""下午场邮件发送脚本 - 2026-02-20"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

# SMTP配置
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "qun.xitang.du@gmail.com"
SMTP_PASSWORD = "kgcokoehjimwlvcv"

# 收件人
TO_EMAIL = "broadbtinp@gmail.com"

# 邮件内容
subject = "🎯 每日猎头任务汇总 - 2026-02-20（下午场）"
body = """# 🎯 每日猎头任务 - 下午场汇总

**日期**: 2026-02-20
**执行时间**: 14:00 (上海时间)
**任务状态**: ✅ 完成

---

## 📊 下午场搜索结果

**新增搜索链接**: 5个
**覆盖平台**: 5个（LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网）

### 新增搜索链接

1. **[LinkedIn] AI产品总监**
   https://www.linkedin.com/jobs/search/?keywords=AI产品总监&location=China

2. **[猎聘] AI产品总监**
   https://www.liepin.com/zhaopin/?key=AI产品总监

3. **[BOSS直聘] AI产品总监**
   https://www.zhipin.com/web/geek/job?query=AI产品总监

4. **[前程无忧] AI产品总监**
   https://search.51job.com/list/000000,000000,0000,00,9,99,AI产品总监,2,1.html

5. **[拉勾网] AI产品总监**
   https://www.lagou.com/wn/zhaopin?kd=AI产品总监

---

## 📋 今日完整汇总

### 上午场（已完成）
- 搜索链接：25个
- 飞书文档：https://feishu.cn/docx/KEXBd56A5oKEcHxXXHicbYR4ncf
- GitHub：commit f4c9a7a

### 下午场（本次）
- 新增链接：5个
- 飞书文档：（即将创建）
- GitHub：（待提交）

### 今日总计
- **搜索链接总数**：30个
- **覆盖平台**：5个
- **目标职位**：AI产品总监、智能家居负责人、AIoT战略

---

## 🎯 建议行动

1. **立即访问**上述新增链接
2. **重点投递**AI产品总监岗位
3. **跟进上午**投递的职位状态
4. **更新简历**根据职位要求微调

---

## 📈 进展追踪

**今日投递**: _待填写_
**已获面试**: _待填写_
**跟进机会**: _待填写_

---

**AI Headhunter Assistant**
**报告生成时间**: 2026-02-20 14:00 (上海时间)
"""

# 创建邮件
msg = MIMEMultipart()
msg['From'] = SMTP_USER
msg['To'] = TO_EMAIL
msg['Subject'] = subject
msg['Date'] = formatdate(localtime=True)
msg.attach(MIMEText(body, 'plain', 'utf-8'))

# 发送邮件
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(SMTP_USER, [TO_EMAIL], msg.as_string())
    server.quit()
    print("✅ 邮件发送成功！")
    print(f"📧 收件人: {TO_EMAIL}")
    print(f"📋 主题: {subject}")
except Exception as e:
    print(f"❌ 邮件发送失败: {e}")
