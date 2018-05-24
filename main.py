import json
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='')

countries = { 'us': 'United States', 'ar': 'Argentina', 'es': 'Spain'}

sources = newsapi.get_sources(language='es')
limit = 5

for source in sources['sources']:
    print('ID: ' + source['id'] + ', Name: ' + source['name'] + ', Country: ' + countries[source['country']])
    print(str(limit) + ' most recent articles:')
    articles = newsapi.get_everything(sources=source['id'],
                                      language='es',
                                      sort_by='relevancy')
    for index, article in enumerate(articles['articles']):
        print('\tTitle: ' + article['title'])
        print('\tLink: ' + article['url'])
        if index == limit:
            break
