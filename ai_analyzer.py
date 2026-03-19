import google.generativeai as genai
import json
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-pro")

def analyze_news(news_list):
    analyzed = []

    for news in news_list:
        prompt = f"""
        다음 IT 뉴스를 한 줄로 요약하고 중요도를 판단해줘.

        제목: {news['title']}
        내용: {news['summary']}

        출력 형식:
        요약:
        중요도: (상/중/하)
        """

        response = model.generate_content(prompt)

        analyzed.append({
            "title": news["title"],
            "summary": response.text,
            "date": news["published"]
        })

    with open("data/analyzed.json", "w", encoding="utf-8") as f:
        json.dump(analyzed, f, ensure_ascii=False, indent=2)

    return analyzed