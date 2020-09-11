import scrapy
import re


class imdb(scrapy.Spider):
    name = "imdb"

    def start_requests(self):
        urls = [
            'https://www.imdb.com/list/ls020465507/?sort=list_order,asc&mode=detail&page=1',
            ]

        for url in urls:

            yield scrapy.Request(url=url,

                callback=self.parse_search,
                meta={
                    'page': 1,
                    'siteName': 'Teletime'
                }
            )

    def parse_search(self, response):
        pageload = response.css('h1::text').get()
        if pageload is not None:
            self.log( "Page Exists! Or at least one 'row' did.. " )
        listOrder = 0
        for product in response.css('.lister-item.mode-detail'):
            listOrder = listOrder + 1
            vars = {}
            vars['name'] =product.css('h3 a::text').get()
            vars['model'] = product.css('.list-description p::text').get().split(' ')[1]
            vars['picture'] = product.css('.lister-item-image a img::attr(src)').get()
            vars['listOrder'] = listOrder

            yield vars
               