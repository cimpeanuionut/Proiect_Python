from Clustering import Clustering
from Constants import Constants
from Crawler import Crawler
from FileUtils import FileUtils


def main():
    crawler = Crawler()
    file_utils = FileUtils()
    clustering = Clustering()

    article_list = crawler.getArticleList(Constants.url)
    article_items = crawler.crawl(article_list)
    file_utils.writeToTxt(article_items)
    row_names, col_names, data = file_utils.readFromTxt(Constants.file_name)
    clustering.acluster(row_names, col_names, data)


if __name__ == '__main__':
    main()
