import streamlit as st
import json
from rss_collector import collect_rss
from ai_analyzer import analyze_news

st.title("🔧 관리자 대시보드")

password = st.text_input("비밀번호", type="password")

if password == "1234":

    st.subheader("RSS 관리")

    with open("data/feeds.json", "r+") as f:
        feeds = json.load(f)

    new_feed = st.text_input("RSS URL 추가")

    if st.button("추가"):
        feeds.append(new_feed)
        with open("data/feeds.json", "w") as f:
            json.dump(feeds, f)

    st.write(feeds)

    if st.button("RSS 수집"):
        news = collect_rss(feeds)
        st.success("수집 완료")

    if st.button("AI 분석"):
        with open("data/raw_news.json") as f:
            news = json.load(f)

        analyze_news(news)
        st.success("분석 완료")

    st.subheader("접속자 수")

    with open("data/visitors.json") as f:
        visitors = json.load(f)

    st.write(len(visitors))

else:
    st.warning("접근 불가")