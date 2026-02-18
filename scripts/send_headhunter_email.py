#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日猎头任务汇总邮件 - 2026-02-18
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# ============ SMTP 配置 ============
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
APP_PASSWORD = "kgcokoehjimwlvcv"

RECEIVERS = ["broadbtinp@gmail.com"]

# ============ 邮件内容 ============
EMAIL_SUBJECT = "🎯 每日猎头任务汇总 - 2026-02-18（下午场）"

EMAIL_BODY = """你好！

这是2026年2月18日下午场的猎头任务汇总报告。

## 📊 今日搜索统计

**上午场（10:00）**
- 搜索链接: 25个
- 覆盖平台: 5个 (LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网)
- 目标职位: AI产品总监、智能家居负责人、AIoT战略
- 执行状态: ✅ 已完成

**下午场（14:00）**
- 搜索链接: 25个（新增）
- 执行时间: 2026-02-18 14:00:23
- 执行状态: ✅ 已完成

## 🎯 重点平台

1. **LinkedIn** (国际化公司)
   - AI产品总监、AI Product Director
   - 智能家居负责人、Smart Home Lead
   - AIoT战略负责人

2. **猎聘** (中高端职位)
   - 同上5个职位类型

3. **BOSS直聘** (快速响应)
   - 同上5个职位类型

4. **前程无忧** (传统渠道)
   - 同上5个职位类型

5. **拉勾网** (互联网+AI)
   - 同上5个职位类型

## 🏢 目标公司清单

**国内大厂**: 华为、小米、字节跳动、阿里巴巴、腾讯、百度、美团、京东

**智能家居**: 海尔、美的、格力、TCL、海信

**AI/机器人**: 科大讯飞、涂鸦智能、大疆、优必选、科沃斯、石头科技、追觅、云鲸

**造车新势力**: 蔚来、小鹏、理想

**外企**: 博世、西门子、伊莱克斯、三星、LG、松下、索尼

## 📝 执行建议

1. 立即访问上述搜索链接，筛选合适的职位
2. 重点关注大厂和外企的AI产品总监岗位
3. 突出AI产品经验（HomeGPT、AI烤箱、5亿营收成果）
4. 跟进上午投递的职位状态

## 🔗 相关资源

- **飞书文档**: https://feishu.cn/docx/IlIidCNNtowaq6xbWgzcrF1AnZ4
- **GitHub仓库**: https://github.com/DaimaRuge/Du-Qun-Resume
- **简历（中文）**: https://github.com/DaimaRuge/Du-Qun-Resume/blob/main/Du_Qun_Resume_CN_V4.0_Optimized.md
- **简历（英文）**: https://github.com/DaimaRuge/Du-Qun-Resume/blob/main/Du_Qun_Resume_EN_V4.0_Optimized.md

---

**任务执行**: AI猎头助手
**日期**: 2026-02-18
**下次执行**: 2026-02-19 10:00（上午场）
"""


def send_email():
    """发送邮件"""
    try:
        msg = MIMEText(EMAIL_BODY, 'plain', 'utf-8')
        msg['From'] = formataddr(("杜群 - AI猎头助手", SENDER_EMAIL))
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
