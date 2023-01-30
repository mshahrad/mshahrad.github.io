# written by Mohammad Shahrad @UBC

RECENT_NEWS_COUNT = 5

import json

with open("./all-news.json") as f:
    allNews = json.load(f)

recent_news_counter = 0
with open("./recent-news.js", "w") as f:
    f.write("document.write('\\\n")
    f.write("<ul>\\\n")
    for value in allNews.values():
        f.write("<li>\\\n")
        date, content = value["date"], value["content"]
        date = date.replace("'", "\\'")
        content = content.replace("'", "\\'")
        f.write(date + " - " + content + "\\\n")
        f.write("</li>\\\n")
        recent_news_counter += 1
        if recent_news_counter >= RECENT_NEWS_COUNT:
            break
    f.write("</ul>\\\n")
    f.write("');")

with open("./all-news.js", "w") as f:
    f.write("document.write('\\\n")
    f.write("<ul>\\\n")
    for value in allNews.values():
        f.write("<li>\\\n")
        date, content = value["date"], value["content"]
        date = date.replace("'", "\\'")
        content = content.replace("'", "\\'")
        f.write(date + " - " + content + "\\\n")
        f.write("</li>\\\n")
    f.write("</ul>\\\n")
    f.write("');")
