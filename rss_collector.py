import feedparser
import json
from datetime import datetime

def collect_rss(feed_urls):
    all_news = []

    for url in feed_urls:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            news = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", ""),
                "summary": entry.get("summary", ""),
                "collected_at": datetime.now().isoformat()
            }
            all_news.append(news)

    with open("data/raw_news.json", "w", encoding="utf-8") as f:
        json.dump(all_news, f, ensure_ascii=False, indent=2)

    return all_news