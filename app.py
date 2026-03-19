import streamlit as st
import json
from datetime import datetime

st.title("🧠 AI 뉴스룸")

# 방문자 기록
with open("data/visitors.json", "r+") as f:
    data = json.load(f)
    data.append({"time": datetime.now().isoformat()})
    f.seek(0)
    json.dump(data, f)

# 뉴스 로딩
with open("data/analyzed.json", "r", encoding="utf-8") as f:
    news = json.load(f)

# 날짜별 정리
grouped = {}

for n in news:
    date = n["date"][:10]
    if date not in grouped:
        grouped[date] = []
    grouped[date].append(n)

for date, items in grouped.items():
    st.header(f"📅 {date}")

    for item in items:
        st.write(f"### {item['title']}")
        st.write(item['summary'])