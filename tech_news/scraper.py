import time
import requests
from requests.exceptions import Timeout
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css(".tec--article__header__title::text").get()
    writer = selector.css(".tec--author__info__link::text").get()
    writer = writer.strip() if writer else None
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    shares_count = int(shares_count) if shares_count else 0
    comments_count = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    comments_count = int(comments_count) if comments_count else 0
    summary = selector.css(
        ".tec--article__body p:nth-child(1) *::text"
    ).getall()
    summary = "".join(summary)
    sources = selector.css(".z--mb-16 .tec--badge::text").getall()
    sources = [source.strip() for source in sources]
    categories = selector.css("#js-categories  a::text").getall()
    categories = [category.strip() for category in categories]
    result = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": shares_count,
        "comments_count": comments_count,
        "summary": summary,
        "sources": sources,
        "categories": categories
    }
    return result


# Requisito 3
def scrape_novidades(html_content):
    select = parsel.Selector(html_content)
    list_url = select.css(
        "div.tec--card__info h3 a::attr(href)"
    ).getall()
    return list_url


# Requisito 4
def scrape_next_page_link(html_content):
    select = parsel.Selector(html_content)
    next_page_link = select.css("a.tec--btn.tec--btn--lg::attr(href)").get()
    return next_page_link


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    data = []
    while url:
        response = fetch(url)
        list = scrape_novidades(response)
        for notice in list:
            response_news = fetch(notice)
            item = scrape_noticia(response_news)
            data.append(item)
            if amount == len(data):
                create_news(data)
                return data
        url = scrape_next_page_link(response)
