import requests
from pyquery import PyQuery as pq
from Article import Article


class Crawler:
    def __init__(self):
        pass

    # Functia returneaza o lista cu linkurile articolelor
    def getArticleList(self, url):
        print('crawling: ' + url)
        dom = pq(requests.get(url).text)
        all_elements = dom('a')
        article_elements = []
        for element in all_elements:
            link = pq(element).attr('href')
            if isinstance(link, str):
                if '/news/' in link and link.endswith('.html'):
                    article_elements.append(url + link)

        return list(dict.fromkeys(article_elements))

    # Functia ce va face crawling in toate articolele din standard.co.uk
    def crawl(self, article_list):
        article_items = []
        for article in article_list[:10]:
            print('article: ' + article)
            dom = pq(requests.get(article).text)
            title = dom('title').text()
            number_words_title = len(title.split())
            all_app_integrate_number = dom('.icon').length
            all_number_popular_news = dom('amp-list').length

            article = Article()
            article.title = title
            article.number_words_title = number_words_title
            article.all_app_integrate_number = all_app_integrate_number
            article.all_number_popular_news = all_number_popular_news

            article_items.append(article)

        return article_items
