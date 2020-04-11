from newspaper import Article
import csv
import tldextract

# Metadata:

# twitter account, stock, url, source, title, authors, 
# publish_date, text, and keywords.

# Diverse News Sources for Testing:

# CNN, Yahoo Finance, Wall Street Journal, Bloomberg, CNBC, Reuters, 
# Marketwatch, Financial times, Kiplinger, Motley Fool, Invester Times Daily, 

# function that takes in url parameter and saves metadata to csv file
def getArticleMetadata(url):
    article_info_dict = {}
    article = Article(url)
    article.download()
    article.parse()
    # extracts domain name from the news source URL
    extracted_url = tldextract.extract(url)
    # saves data to a dictionary
    article_info_dict['url'] = url
    article_info_dict['source'] = extracted_url.domain
    article_info_dict['title'] = article.title
    article_info_dict['authors'] = article.authors
    article_info_dict['publish_date'] = article.publish_date
    print()
    print(article_info_dict)
    
    # saves dictionary to csv file
    with open('metadata.csv', 'a', newline='') as csv_file:
        fieldnames = ['twitter_account', 'stock', 'url', 'source', 'title', 'authors', 'publish_date', 'text', 'keywords']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(article_info_dict)

# Testing One URL
url = 'https://www.cnn.com/2020/03/16/tech/amazon-shipping-coronavirus/index.html'
getArticleMetadata(url)

# Testing Multiple URLs
# url_list = ['https://www.cnn.com/2020/03/16/tech/amazon-shipping-coronavirus/index.html',
#             'https://finance.yahoo.com/news/apocalyptic-scenario-unlikely-amazon-other-tech-stocks-tech-analyst-says-194143166.html',
#             'https://www.wsj.com/articles/coronavirus-sparks-hiring-spree-for-nearly-500-000-jobs-at-biggest-retailers-11584984596',
#             'https://www.bloomberg.com/opinion/articles/2020-04-01/apple-deal-with-amazon-prime-video-is-game-changer',
#             'https://www.cnbc.com/2020/03/29/amazon-workers-in-staten-island-plan-strike-over-coronavirus-safety.html',
#             'https://www.reuters.com/article/us-health-coronavirus-amazon-com-masks-e/exclusive-amazon-to-deploy-masks-and-temperature-checks-for-workers-by-next-week-idUSKBN21K1Y6',
#             'https://www.marketwatch.com/story/as-coronavirus-hits-hard-amazon-starts-licensing-cashier-free-technology-to-retailers-2020-03-31',
#             'https://www.ft.com/content/220bf850-726c-11ea-ad98-044200cb277f',
#             'https://www.kiplinger.com/slideshow/investing/T018-S001-the-9-best-dow-jones-dividend-growth-stocks/index.html',
#             'https://www.fool.com/investing/2020/04/02/india-coronavirus-lockdown-mean-amazon-walmart.aspx',
#             'https://www.investors.com/research/how-to-find-the-best-stocks-to-buy/amazon-stock-aws-cloud-services-drive-coronavirus-stock-market/'
#             ]

# for url in url_list:
#     getArticleMetadata(url)

