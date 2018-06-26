import scrapy
from with_html_scrapy_way.fuckWechatVotes.fuckWechatVotes.items import WechatVoteArticle
from six.moves.urllib_parse import quote_plus
from scrapy.conf import settings
from with_html_scrapy_way.fuckWechatVotes.fuckWechatVotes.utils.transcookie import transCookie
from scrapy.http import HtmlResponse, Request
import requests
import re


class WechatVoteSpider(scrapy.Spider):
    name = "wechatVoteSpider"
    allowed_domains = ["weixin.sogou.com"]
    article_query_url = 'http://weixin.sogou.com/weixin?query={keyword}&_sug_type_=&s_from=input&_sug_=n&type=2&page={page}&ie=utf8'
    public_query_url = 'http://weixin.sogou.com/weixin?query={keyword}&_sug_type_=&s_from=input&_sug_=n&type=1&page={page}&ie=utf8'
    start_urls = []
    trans = transCookie(settings['COOKIES'])
    cookies = trans.stringToDict()
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400'
    }

    def __init__(self, *args, **kwargs):
        self.keyword = quote_plus(kwargs.get("k", "投票"))

        super(WechatVoteSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        self.start_urls.append(self.article_query_url.format(keyword=self.keyword, page='1'))
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        ss = response.xpath('//*[@id="pagebar_container"]/div/text()').extract()
        allTiticle = re.findall(r'[0-9]\d*', ss[0])
        allNum = ''
        for ii in allTiticle:
            allNum += ii
        allNumInt = int(allNum)
        for yy in range(0, 100):
            url = self.article_query_url.format(keyword=self.keyword, page=yy)
            # yield Request(url=item0['cityUrl'],
            #               meta={'cityName': item0['cityPinyin']},
            #               callback=self.parse_per_bus_num_list)
            yield Request(url=url, callback=self.parse_get_all_num, cookies=self.cookies, headers=self.headers)

    def parse_get_all_num(self, response):
        allUrl = response.xpath('//div[@id="main"]/div[@class="news_box"]/ul[@class="news-list"]/li')
        for iii in allUrl:
            item = WechatVoteArticle()
            item["url"] = iii.xpath('div[@class="txt-box"]/h3/a[1]/@href').extract()
            item["abstract"] = iii.xpath('//*[@class="txt-info""]').extract()

            # titleP = iii.xpath('div[@class="txt-box"]/h3/a[0]/em')
            # title = ""
            # for perTitle in titleP:
            #     title += perTitle.xpath('text()')
            # item["title"] = title
            # abstractP = iii.xpath('div[@class="txt-box"]/p[@class="txt-info"]/em')
            # abstract = ""
            # for perAbstract in abstractP:
            #     title += perAbstract.xpath('text()')
            # item["abstract"] = abstract
            # item["to_public_name"] = iii.xpath('div[@class="txt-box"]/div[@class="s-p"]/a/test()')
            # item["to_public_url"] = iii.xpath('div[@class="txt-box"]/div[@class="s-p"]/a/@href')
            # item["publish_time"] = iii.xpath('div[@class="txt-box"]/div[@class="s-p"]/span[@class="s2"]/test()')
            yield Request(url=item["url"], callback=self.get_per_page_info_with_award, cookies=self.cookies,
                          headers=self.headers)

    def get_per_page_info_with_award(self, response):
        item = WechatVoteArticle()
        item["url"]=response.url
        item["title"] = response.xpath('//*[@id="activity-name"]/text()')
        item["publish_time"]=response.xpath('//*[@id="publish_time"]/text()')
        item["to_public_num"]=response.xpath('//*[@id="js_profile_qrcode"]/div/p[1]/span/text()')
        item["to_public_name"]=response.xpath('//*[@id="js_name"]/text()')
        item["to_public_des"]=response.xpath('//*[@id="js_profile_qrcode"]/div/p[2]/span/text()')


        yield item

    # id = scrapy.Field()
    # title = scrapy.Field()
    # abstract = scrapy.Field()
    # url = scrapy.Field()
    #
    #
    # publish_time = scrapy.Field()
    # allText = scrapy.Field()
    # to_public_name = scrapy.Field()
    # to_public_num = scrapy.Field()
    # to_public_des = scrapy.Field()
    #
    # award_des = scrapy.Field()
