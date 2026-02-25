#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日猎头任务汇总邮件 - 2026-02-25 下午场
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
EMAIL_SUBJECT = "🎯 每日猎头任务汇总 - 2026-02-25（下午场）"

EMAIL_BODY = """你好！

这是2026年2月25日下午场的猎头任务汇总报告。

## 📊 今日搜索统计

**上午场（10:00）+ 下午场（14:00）**
- 搜索链接: 25个 × 2次 = 50个
- 覆盖平台: 5个 (LinkedIn、猎聘、BOSS直聘、前程无忧、拉勾网)
- 目标职位: AI产品总监、智能家居负责人、AIoT战略
- 执行状态: ✅ 已完成

## 🎯 重点平台搜索链接

### LinkedIn (国际化公司)
- AI产品总监: https://www.linkedin.com/jobs/search/?keywords=AI产品总监&location=China
- AI Product Director: https://www.linkedin.com/jobs/search/?keywords=AI Product Director&location=China
- 智能家居负责人: https://www.linkedin.com/jobs/search/?keywords=智能家居负责人&location=China
- Smart Home Lead: https://www.linkedin.com/jobs/search/?keywords=Smart Home Lead&location=China

### 猎聘 (中高端职位)
- AI产品总监: https://www.liepin.com/zhaopin/?key=AI产品总监
- 智能家居负责人: https://www.liepin.com/zhaopin/?key=智能家居负责人
- AIoT战略负责人: https://www.liepin.com/zhaopin/?key=AIoT战略负责人

### BOSS直聘 (快速响应)
- AI产品总监: https://www.zhipin.com/web/geek/job?query=AI产品总监
- 智能家居负责人: https://www.zhipin.com/web/geek/job?query=智能家居负责人

## 🏢 目标公司清单

**S级（高度匹配）**:
- 涂鸦智能、绿米Aqara、华为、小米、科沃斯

**A级（重点关注）**:
- 海尔、美的、博世、追觅、石头科技、大疆、优必选
- 蔚来、小鹏、理想（智能座舱方向）
- 三星、LG、松下（外企智能家居）

**国内大厂**: 字节跳动、阿里巴巴、腾讯、百度、美团、京东

## 📝 下午执行建议

1. **跟进上午投递** (15分钟)
   - 检查投递平台消息通知
   - 回复HR的即时消息
   - 记录投递反馈

2. **新职位搜索** (30分钟)
   - LinkedIn: 筛选Director/VP级别，200人以上公司
   - 猎聘: 薪资50万+，智能家居/AI/机器人
   - BOSS直聘: 与5个HR建立联系

3. **投递策略**
   - 突出AI产品+智能家电双重背景
   - 强调0-1业务操盘能力
   - 量化成果（5亿营收、$1000万成本优化）

## 📊 今日进展

- [ ] 已投递职位数：待更新
- [ ] 已获得面试：暂无
- [ ] 值得跟进的机会：待更新

## 🔗 相关资源

- **GitHub仓库**: https://github.com/DaimaRuge/Du-Qun-Resume
- **今日报告**: https://github.com/DaimaRuge/Du-Qun-Resume/blob/main/Headhunter_Reports/daily_progress_2026-02-25_afternoon.md
- **简历（中文）**: https://github.com/DaimaRuge/Du-Qun-Resume/blob/main/Du_Qun_Resume_CN_V4.0_Optimized.md
- **简历（英文）**: https://github.com/DaimaRuge/Du-Qun-Resume/blob/main/Du_Qun_Resume_EN_V4.0_Optimized.md

---

**任务执行**: AI猎头助手
**日期**: 2026-02-25
**下次执行**: 2026-02-26 10:00（明日上午场）
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
