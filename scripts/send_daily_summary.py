#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
发送每日猎头任务汇总邮件
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from datetime import datetime

# 邮件配置
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qun.xitang.du@gmail.com"
SENDER_PASSWORD = "kgcokoehjimwlvcv"
SENDER_NAME = "AI猎头助手"

# 收件人
RECIPIENTS = [
    {"email": "broadbtinp@gmail.com", "name": "杜群"},
    {"email": "dulie@foxmail.com", "name": "杜列"}
]

def send_email():
    """发送每日汇总邮件"""
    today = datetime.now().strftime("%Y年%m月%d日")
    
    # 创建邮件
    msg = MIMEMultipart('alternative')
    msg['From'] = formataddr((SENDER_NAME, SENDER_EMAIL))
    msg['To'] = ", ".join([r['email'] for r in RECIPIENTS])
    msg['Subject'] = f"🎯 AI猎头任务日报 - {today}"
    
    # 纯文本内容
    text_content = f"""
AI猎头任务每日汇总 - {today}

亲爱的用户，

今日（{today}）的AI猎头任务已完成，以下是进展汇总：

【执行情况】
✅ 上午10:00搜索 - 已完成
✅ 下午14:00搜索 - 已完成
✅ 总计搜索3次，生成75个职位搜索链接

【覆盖平台】
- LinkedIn（15个链接）
- 猎聘（15个链接）
- BOSS直聘（15个链接）
- 前程无忧（15个链接）
- 拉勾网（15个链接）

【重点方向】
1. AI产品总监/负责人
2. 智能家居产品管理
3. AIoT战略负责人
4. 智能硬件产品

【目标公司】
- 大厂：华为、小米、字节、阿里、腾讯等
- 智能家居：海尔、美的、涂鸦、绿米、欧瑞博等
- 机器人/AI：科大讯飞、大疆、科沃斯、石头等
- 外企：博世、西门子、三星、LG等

【待办事项】
⏳ 需要您访问搜索链接投递简历
⏳ 记录投递职位信息
⏳ 跟进投递反馈

【详细报告】
完整报告已保存至：
/root/.openclaw/workspace/Headhunter_Reports/daily_summary_2026-02-13.md

【简历资源】
GitHub: https://github.com/DaimaRuge/Du-Qun-Resume
- 中文版: Du_Qun_Resume_CN_V4.0_Optimized.md
- 英文版: Du_Qun_Resume_EN_V4.0_Optimized.md

【投递建议】
1. 优先投递：AI产品总监、智能家居负责人
2. 使用V4.0优化版简历
3. 强调AI实战经验和量化成果

---
AI猎头助手
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
    
    # HTML内容
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px 10px 0 0;
            text-align: center;
        }}
        .content {{
            background: #f9f9f9;
            padding: 30px;
            border-radius: 0 0 10px 10px;
        }}
        .section {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .status-done {{
            color: #10b981;
            font-weight: bold;
        }}
        .status-pending {{
            color: #f59e0b;
            font-weight: bold;
        }}
        .highlight {{
            background: #fef3c7;
            padding: 15px;
            border-left: 4px solid #f59e0b;
            margin: 15px 0;
        }}
        ul {{
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 8px;
        }}
        .emoji {{
            font-size: 1.2em;
        }}
        a {{
            color: #667eea;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
            color: #6b7280;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1><span class="emoji">🎯</span> AI猎头任务日报</h1>
        <p>{today}</p>
    </div>
    
    <div class="content">
        <div class="section">
            <h2><span class="emoji">📊</span> 今日执行情况</h2>
            <ul>
                <li><span class="status-done">✅</span> 上午10:00搜索任务</li>
                <li><span class="status-done">✅</span> 下午14:00搜索任务</li>
                <li><span class="status-done">✅</span> 生成75个职位搜索链接</li>
                <li><span class="status-done">✅</span> 覆盖5个主要招聘平台</li>
            </ul>
        </div>
        
        <div class="section">
            <h2><span class="emoji">🔍</span> 搜索覆盖</h2>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="background: #f3f4f6;">
                    <th style="padding: 10px; text-align: left;">平台</th>
                    <th style="padding: 10px; text-align: center;">链接数</th>
                    <th style="padding: 10px; text-align: left;">特点</th>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">LinkedIn</td>
                    <td style="padding: 10px; text-align: center; border-bottom: 1px solid #e5e7eb;">15</td>
                    <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">国际化公司</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">猎聘</td>
                    <td style="padding: 10px; text-align: center; border-bottom: 1px solid #e5e7eb;">15</td>
                    <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">中高端职位</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">BOSS直聘</td>
                    <td style="padding: 10px; text-align: center; border-bottom: 1px solid #e5e7eb;">15</td>
                    <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">快速响应</td>
                </tr>
                <tr>
                    <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">前程无忧</td>
                    <td style="padding: 10px; text-align: center; border-bottom: 1px solid #e5e7eb;">15</td>
                    <td style="padding: 10px; border-bottom: 1px solid #e5e7eb;">传统大厂</td>
                </tr>
                <tr>
                    <td style="padding: 10px;">拉勾网</td>
                    <td style="padding: 10px; text-align: center;">15</td>
                    <td style="padding: 10px;">互联网行业</td>
                </tr>
            </table>
        </div>
        
        <div class="section">
            <h2><span class="emoji">🎯</span> 重点职位方向</h2>
            <ul>
                <li><strong>AI产品总监/负责人</strong> - 最高优先级 ⭐⭐⭐⭐⭐</li>
                <li><strong>智能家居产品管理</strong> - 最高优先级 ⭐⭐⭐⭐⭐</li>
                <li><strong>AIoT战略负责人</strong> - 高优先级 ⭐⭐⭐⭐</li>
                <li><strong>智能硬件产品</strong> - 高优先级 ⭐⭐⭐⭐</li>
            </ul>
        </div>
        
        <div class="section">
            <h2><span class="emoji">🏢</span> 目标公司</h2>
            <p><strong>大厂：</strong>华为、小米、字节跳动、阿里巴巴、腾讯、百度、美团、京东</p>
            <p><strong>智能家居：</strong>海尔、美的、格力、涂鸦智能、绿米、欧瑞博</p>
            <p><strong>机器人/AI：</strong>科大讯飞、大疆、科沃斯、石头科技、追觅</p>
            <p><strong>外企：</strong>博世、西门子、三星、LG、松下</p>
        </div>
        
        <div class="highlight">
            <h3><span class="emoji">⏳</span> 待办事项（需要您的操作）</h3>
            <ul>
                <li>访问搜索链接投递简历</li>
                <li>记录投递职位信息</li>
                <li>跟进投递反馈</li>
                <li>准备面试（如有）</li>
            </ul>
        </div>
        
        <div class="section">
            <h2><span class="emoji">💡</span> 投递建议</h2>
            <ol>
                <li>使用 <strong>V4.0优化版简历</strong>，突出AI实战经验</li>
                <li>强调量化成果：5亿营收、$1000万成本优化</li>
                <li>重点投递：AI产品总监、智能家居负责人职位</li>
                <li>优先平台：猎聘（中高端）、LinkedIn（国际）</li>
            </ol>
            <p style="margin-top: 15px;">
                <a href="https://github.com/DaimaRuge/Du-Qun-Resume">📄 GitHub简历仓库</a>
            </p>
        </div>
    </div>
    
    <div class="footer">
        <p>AI猎头助手 | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p>下次执行时间：2026-02-14 10:00 (UTC+8)</p>
    </div>
</body>
</html>
"""
    
    # 添加内容
    part1 = MIMEText(text_content, 'plain', 'utf-8')
    part2 = MIMEText(html_content, 'html', 'utf-8')
    msg.attach(part1)
    msg.attach(part2)
    
    # 发送邮件
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        for recipient in RECIPIENTS:
            server.sendmail(
                SENDER_EMAIL,
                recipient['email'],
                msg.as_string()
            )
            print(f"✅ 邮件已发送至: {recipient['name']} <{recipient['email']}>")
        
        server.quit()
        print("\n✅ 所有邮件发送成功！")
        return True
    except Exception as e:
        print(f"❌ 发送失败: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("📧 发送每日猎头任务汇总邮件")
    print("=" * 60)
    send_email()
