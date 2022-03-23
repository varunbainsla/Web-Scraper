import scrapy
from items import WebscrapeItem

class TechSpider(scrapy.Spider):
    name = 'tech'
    allowed_domains = ['techcrunch.com']
    start_urls = ['http://techcrunch.com/']

    def parse(self, response):
        c=response.css('.content a::attr(href)').getall()
        for i in c:
            i=response.urljoin(i)
            
            yield scrapy.Request(url=i,callback=self.parse_content)



    def parse_content(self,response):

        item = WebscrapeItem()
        Title=response.css('h1.article__title::text').extract()
        Author=response.css('div.article__byline a::text').extract()
        post=response.css('div.article-content ::text').extract()
            
        item['title']= Title
        item['author']=Author
        item['post']=post
            
        yield item
         
