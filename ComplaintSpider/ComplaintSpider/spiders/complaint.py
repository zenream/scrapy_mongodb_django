# -*- coding: utf-8 -*-
import scrapy
from ComplaintSpider.items import ComplaintspiderItem

class ComplaintSpider(scrapy.Spider):
    name = 'complaint'
    # 设置爬取的域名范围，可省略，不写则表示爬取时候不限域名，结果有可能会导致爬虫失控
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url + str(offset)]

    # 解析返回的网页数据，提取结构化数据，生成需要下一页的URL请求
    def parse(self, response):
        # 取出每个页面里帖子链接列表
        links = response.xpath("//div[@class='greyframe']/table//td/a[@class='news14']/@href").extract()
        # 迭代发送每个帖子的请求，调用 parse_item 方法处理
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)

        # 设置页码终止条件，并且每次发送新的页面请求调用 parse 方法处理
        if self.offset <= 71130:
            self.offset += 30
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    # 封装数据
    def parse_item(self, response):
        # 将得到的数据封装到 SunspiderItem
        item = ComplaintspiderItem()
        # 标题
        item['title'] = response.xpath('//div[contains(@class,"pagecenter p3")]//strong/text()').extract()[0]
        # 编号
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]
        # 文字内容，默认先取出有图片情况下的文字内容列表
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        # 若没有内容，则取出没有图片情况下的文字内容列表
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            # content 为列表，通过 join 方法拼接为字符串，并去除首尾空格
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()

        # 链接
        item['url'] = response.url
        yield item

