import scrapy
import datetime
from ..items import AdcspiderItem


class VipspiderSpider(scrapy.Spider):
    name = 'vipspider'
    allowed_domains = ['yglz.tousu.hebnews.cn/']
    start_urls = ['http://yglz.tousu.hebnews.cn/shss-1.html']
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }
    pageCount = 1

    def parse(self, response):
        startTime = datetime.datetime.now()
        print('----------------------')
        item = AdcspiderItem()
        for i in range(1, 21):
            for each in response.xpath('//*[@id="divList"]/div[' + str(i) + ']'):
                newsType = each.xpath('./span[2]/p/text()').extract_first()
                newsTitle = each.xpath('./span[3]/p/a/text()').extract_first()
                newsTime = each.xpath('./span[4]/p/text()').extract_first()
                if '石家庄' in newsTitle:
                    print('分类:', newsType, '标题:', newsTitle, '时间:', newsTime)
                    item['newsType'] = newsType
                    item['newsTitle'] = newsTitle
                    item['newsTime'] = newsTime
                    yield item
        self.pageCount = self.pageCount + 1
        if self.pageCount < 20:
            next_url = 'http://yglz.tousu.hebnews.cn/shss-' + str(self.pageCount) + '.html'
            print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
        endTime = datetime.datetime.now()
        print('运行时间：', (endTime - startTime).seconds)
        # next_no = response.xpath('//*[@id="divList"]/div[21]/a[1]/@onclick').extract()
        # arr = next_no[0].split('|')
        # pageNo = arr[2][0:1]
        # if pageNo and int(pageNo) < 4:
        #     next_url = 'http://yglz.tousu.hebnews.cn/shss-'+pageNo+'.html'
        #     print(next_url)
        #     yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
