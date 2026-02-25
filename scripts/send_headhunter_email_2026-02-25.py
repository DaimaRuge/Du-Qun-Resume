#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日猎头任务汇总邮件 - 2026-02-25
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from datetime import datetime

# ============ SMTP 配置 ============
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
APP_PASSWORD = "kgcokoehjimwlvcv"

RECEIVERS = ["broadbtinp@gmail.com"]

# ============ 邮件内容 ============
EMAIL_SUBJECT = "🎯 每日猎头任务汇总 - 2026-02-25（上午场）"

EMAIL_BODY = """你好！

这是2026年2月25日上午场的猎头任务汇总报告。

## 📊 今日搜索统计

**执行时间**: 2026-02-25 10:00:10
**搜索链接**: 25个
**覆盖平台**: 5个 (LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网)
**目标职位**: AI产品总监、智能家居负责人、AIoT战略负责人

## 🔍 搜索链接清单

### LinkedIn（国际化公司）
- AI产品总监: https://www.linkedin.com/jobs/search/?keywords=AI产品总监&location=China
- AI Product Director: https://www.linkedin.com/jobs/search/?keywords=AI%20Product%20Director&location=China
- 智能家居负责人: https://www.linkedin.com/jobs/search/?keywords=智能家居负责人&location=China
- Smart Home Lead: https://www.linkedin.com/jobs/search/?keywords=Smart%20Home%20Lead&location=China
- AIoT战略负责人: https://www.linkedin.com/jobs/search/?keywords=AIoT战略负责人&location=China

### 猎聘（中高端职位）
- AI产品总监: https://www.liepin.com/zhaopin/?key=AI产品总监
- AI Product Director: https://www.liepin.com/zhaopin/?key=AI%20Product%20Director
- 智能家居负责人: https://www.liepin.com/zhaopin/?key=智能家居负责人
- Smart Home Lead: https://www.liepin.com/zhaopin/?key=Smart%20Home%20Lead
- AIoT战略负责人: https://www.liepin.com/zhaopin/?key=AIoT战略负责人

### BOSS直聘（快速响应）
- AI产品总监: https://www.zhipin.com/web/geek/job?query=AI产品总监
- AI Product Director: https://www.zhipin.com/web/geek/job?query=AI%20Product%20Director
- 智能家居负责人: https://www.zhipin.com/web/geek/job?query=智能家居负责人
- Smart Home Lead: https://www.zhipin.com/web/geek/job?query=Smart%20Home%20Lead
- AIoT战略负责人: https://www.zhipin.com/web/geek/job?query=AIoT战略负责人

### 前程无忧（传统渠道）
- AI产品总监: https://search.51job.com/list/000000,000000,0000,00,9,99,AI产品总监,2,1.html
- 智能家居负责人: https://search.51job.com/list/000000,000000,0000,00,9,99,智能家居负责人,2,1.html
- AIoT战略负责人: https://search.51job.com/list/000000,000000,0000,00,9,99,AIoT战略负责人,2,1.html

### 拉勾网（互联网+AI）
- AI产品总监: https://www.lagou.com/wn/zhaopin?kd=AI产品总监
- 智能家居负责人: https://www.lagou.com/wn/zhaopin?kd=智能家居负责人
- AIoT战略负责人: https://www.lagou.com/wn/zhaopin?kd=AIoT战略负责人

## 🏢 目标公司清单

**国内大厂**: 华为、小米、字节跳动、阿里巴巴、腾讯、百度、美团、京东

**智能家居**: 海尔、美的、格力、TCL、海信、绿米、欧瑞博

**AI/机器人**: 科大讯飞、涂鸦智能、大疆、优必选、科沃斯、石头科技、追觅、云鲸

**造车新势力**: 蔚来、小鹏、理想

**外企**: 博世、西门子、伊莱克斯、惠而浦、三星、LG、松下、索尼

## 📝 执行建议

1. **优先顺序**: LinkedIn → 猎聘 → BOSS直聘 → 前程无忧 → 拉勾网
2. **每日任务**:
   - 上午10:00-11:00：搜索并投递5-10个职位
   - 下午14:00-15:00：跟进投递状态，寻找新机会
3. **投递策略**:
   - 突出AI产品经验（HomeGPT、AI烤箱）
   - 强调0-1业务操盘能力
   - 量化成果（5亿营收、$1000万成本优化）

## 🔗 相关资源

- **GitHub仓库**: https://github.com/DaimaRuge/Du-Qun-Resume
- **简历（中文）**: https://github.com/DaimaRuge/Du-Qun-Resume/blob/main/Du_Qun_Resume_CN_V4.0_Optimized.md
- **简历（英文）**: https://github.com/DaimaRuge/Du-Qun-Resume/blob/main/Du_Qun_Resume_EN_V4.0_Optimized.md

---

**任务执行**: AI猎头助手
**日期**: 2026-02-25
**下次执行**: 2026-02-25 14:00（下午场）
"""


def send_email():
    """发送邮件"""
    try:
        msg = MIMEMultipart()
        msg['From'] = formataddr(("杜群 - AI猎头助手", SENDER_EMAIL))
        msg['To'] = ", ".join(RECEIVERS)
        msg['Subject'] = EMAIL_SUBJECT
        
        msg.attach(MIMEText(EMAIL_BODY, 'plain', 'utf-8'))

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
    print("📧 每日猎头任务汇总 - 邮件发送")
    print("=" * 60)
    print(f"发件人: {SENDER_EMAIL}")
    print(f"收件人: {', '.join(RECEIVERS)}")
    print(f"主题: {EMAIL_SUBJECT}")
    print("=" * 60)
    
    if send_email():
        print("\n✨ 完成！邮件已成功发送。")
    else:
        print("\n❌ 发送失败，请检查配置。")
