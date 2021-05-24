from tech_news.database import find_news


# Requisito 10
def top_5_news():
    search = find_news()
    newsPopularity = []
    for new in search:
        newsPopularity.append({
            "title": new["title"],
            "url": new["url"],
            "popularity": new["shares_count"] + new["comments_count"]
        })

    def mostPopularity(e):
        return e['popularity']

    newsPopularity.sort(key=mostPopularity, reverse=True)

    topFive = []
    for new in newsPopularity:
        topFive.append((new["title"], new["url"]))

    return topFive[0:5]


# Requisito 11
def top_5_categories():
    search = find_news()
    listCategories = set()
    for new in search:
        for category in new['categories']:
            listCategories.add(category)
    topFive = sorted(listCategories)[0:5]
    return topFive
