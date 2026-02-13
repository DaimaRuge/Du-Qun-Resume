#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI猎头任务 - 每日职位搜索与机会挖掘
"""

import json
import os
from datetime import datetime
from pathlib import Path

# 目标职位关键词
TARGET_ROLES = [
    "AI产品总监",
    "AI Product Director",
    "智能家居负责人",
    "Smart Home Lead",
    "AIoT战略负责人",
    "AIoT Strategy Head",
    "产品总监",
    "Product Director",
    "智能硬件产品",
    "Smart Hardware Product"
]

# 搜索平台
PLATFORMS = {
    "linkedin": {
        "name": "LinkedIn",
        "url": "https://www.linkedin.com/jobs/",
        "search_url": "https://www.linkedin.com/jobs/search/?keywords={keyword}&location=China"
    },
    "liepin": {
        "name": "猎聘",
        "url": "https://www.liepin.com/",
        "search_url": "https://www.liepin.com/zhaopin/?key={keyword}"
    },
    "boss": {
        "name": "BOSS直聘",
        "url": "https://www.zhipin.com/",
        "search_url": "https://www.zhipin.com/web/geek/job?query={keyword}"
    },
    "51job": {
        "name": "前程无忧",
        "url": "https://www.51job.com/",
        "search_url": "https://search.51job.com/list/000000,000000,0000,00,9,99,{keyword},2,1.html"
    },
    "lagou": {
        "name": "拉勾网",
        "url": "https://www.lagou.com/",
        "search_url": "https://www.lagou.com/wn/zhaopin?kd={keyword}"
    }
}

# 目标公司（智能家居/AI领域）
TARGET_COMPANIES = [
    # 大厂
    "华为", "Huawei",
    "小米", "Xiaomi",
    "字节跳动", "ByteDance",
    "阿里巴巴", "Alibaba",
    "腾讯", "Tencent",
    "百度", "Baidu",
    "美团", "Meituan",
    "京东", "JD.com",
    
    # 智能家居
    "海尔", "Haier",
    "美的", "Midea",
    "格力", "Gree",
    "TCL",
    "海信", "Hisense",
    "创维", "Skyworth",
    "科大讯飞", "iFlytek",
    "涂鸦智能", "Tuya",
    "绿米", "Aqara",
    "欧瑞博", "ORVIBO",
    
    # 机器人/AI
    "大疆", "DJI",
    "优必选", "UBTECH",
    "科沃斯", "Ecovacs",
    "石头科技", "Roborock",
    "追觅", "Dreame",
    "云鲸", "Narwal",
    
    # 互联网+
    "蔚来", "NIO",
    "小鹏", "XPeng",
    "理想", "Li Auto",
    
    # 外企
    "博世", "Bosch",
    "西门子", "Siemens",
    "伊莱克斯", "Electrolux",
    "惠而浦", "Whirlpool",
    "三星", "Samsung",
    "LG",
    "松下", "Panasonic",
    "索尼", "Sony"
]


def generate_search_links():
    """生成搜索链接"""
    links = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for role in TARGET_ROLES[:5]:  # 取前5个关键词
        for platform_id, platform in PLATFORMS.items():
            search_url = platform["search_url"].format(keyword=role)
            links.append({
                "platform": platform["name"],
                "keyword": role,
                "url": search_url
            })
    
    return links, timestamp


def create_daily_report(links, timestamp):
    """创建每日报告"""
    report_dir = Path("/root/.openclaw/workspace/Headhunter_Reports")
    report_dir.mkdir(exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    report_file = report_dir / f"headhunter_report_{today}.md"
    
    # 检查是否已有报告
    if report_file.exists():
        with open(report_file, 'r', encoding='utf-8') as f:
            existing_content = f.read()
        # 如果今天已有报告，追加新搜索
        mode = "append"
    else:
        existing_content = ""
        mode = "create"
    
    # 生成报告内容
    report_content = f"""
# 🎯 AI猎头任务报告

**执行时间**: {timestamp}
**任务**: 每日职位搜索与机会挖掘

---

## 📋 搜索链接清单

### 按平台分类

"""
    
    # 按平台分组
    platform_groups = {}
    for link in links:
        platform = link["platform"]
        if platform not in platform_groups:
            platform_groups[platform] = []
        platform_groups[platform].append(link)
    
    for platform, platform_links in platform_groups.items():
        report_content += f"#### {platform}\n\n"
        for link in platform_links:
            report_content += f"- [{link['keyword']}]({link['url']})\n"
        report_content += "\n"
    
    report_content += f"""
---

## 🎯 目标公司清单

### 智能家居/AI领域重点公司

"""
    
    # 按类别分组公司
    categories = {
        "大厂": TARGET_COMPANIES[:16],
        "智能家居": TARGET_COMPANIES[16:25],
        "机器人/AI": TARGET_COMPANIES[25:31],
        "互联网+": TARGET_COMPANIES[31:34],
        "外企": TARGET_COMPANIES[34:]
    }
    
    for category, companies in categories.items():
        report_content += f"**{category}**: {', '.join(companies)}\n\n"
    
    report_content += """
---

## 📝 执行建议

1. **优先顺序**:
   - LinkedIn（国际化公司）
   - 猎聘（中高端职位）
   - BOSS直聘（快速响应）
   - 企业官网（直接投递）

2. **每日任务**:
   - [ ] 上午10:00-11:00：搜索并投递5-10个职位
   - [ ] 下午14:00-15:00：跟进投递状态，寻找新机会

3. **重点方向**:
   - AI产品总监/负责人
   - 智能家居产品管理
   - AIoT战略规划
   - 智能硬件创新

4. **投递策略**:
   - 突出AI产品经验（HomeGPT、AI烤箱）
   - 强调0-1业务操盘能力
   - 量化成果（5亿营收、$1000万成本优化）

---

## 📊 今日进展

**待填写**:
- [ ] 已投递职位数：____
- [ ] 已获得面试：____
- [ ] 值得跟进的机会：____

---

**报告生成**: AI Headhunter Assistant
**日期**: {date}
""".format(date=today)
    
    # 写入文件
    if mode == "create":
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
    else:
        # 追加新的搜索记录
        with open(report_file, 'a', encoding='utf-8') as f:
            f.write(f"\n\n---\n\n## 新增搜索 ({timestamp})\n\n")
            for link in links[:5]:  # 只追加前5个
                f.write(f"- [{link['platform']}] {link['keyword']}: {link['url']}\n")
    
    return report_file


def main():
    """主函数"""
    print("=" * 60)
    print("🎯 AI猎头任务 - 每日职位搜索")
    print("=" * 60)
    
    # 生成搜索链接
    links, timestamp = generate_search_links()
    
    # 创建报告
    report_file = create_daily_report(links, timestamp)
    
    print(f"✅ 已生成搜索链接: {len(links)}个")
    print(f"✅ 报告已保存: {report_file}")
    
    # 输出部分链接供参考
    print("\n📋 今日搜索任务:")
    for i, link in enumerate(links[:5], 1):
        print(f"  {i}. [{link['platform']}] {link['keyword']}")
    
    print("\n" + "=" * 60)
    print("💡 建议: 立即开始访问上述链接，投递合适的职位")
    print("=" * 60)


if __name__ == "__main__":
    main()
