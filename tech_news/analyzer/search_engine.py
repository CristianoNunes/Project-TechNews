from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    title_news = search_news({"title": {"$regex": title, "$options": "i"}})
    titleArr = []
    for new in title_news:
        titleArr.append((new["title"], new["url"]))

    return titleArr


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    search = search_news({"timestamp": {"$regex": date}})
    newsArr = []
    for new in search:
        newsArr.append((new["title"], new["url"]))
    return newsArr


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
