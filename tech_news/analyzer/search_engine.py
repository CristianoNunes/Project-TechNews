from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    title_news = search_news({"title": {"$regex": title, "$options": "i"}})
    titleArr = []
    for new in title_news:
        titleArr.append((new["title"], new["url"]))

    return titleArr


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
