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

    def parse_get_all_num(self, response):
        ss = response.xpath('//*[@id="pagebar_container"]/div/text()').extract()
        allTiticle = re.findall(r'[0-9]\d*', ss[0])
        allNum = ''
        for ii in allTiticle:
            allNum += ii
        allNumInt = int(allNum)
        for yy in range(0, allNum / 10):
            url = self.article_query_url.format(keyword=self.keyword, page=yy)
            # yield Request(url=item0['cityUrl'],
            #               meta={'cityName': item0['cityPinyin']},
            #               callback=self.parse_per_bus_num_list)
            yield Request(url=url, callback=self.parse, cookies=self.cookies, headers=self.headers)

        def parse(self, response):
            allUrl=response.xpath('//div[@id="main"]/div[@class="news_box"]/ul[@class="news-list"]/li')
            for iii in allUrl:
                item=WechatVoteArticle()
                item["url"]=iii.xpath('div[@class="txt-box"]/h3/a[0]/@href').extract()
                item["url"]=iii.xpath('div[@class="txt-box"]/h3/a[0]/@href').extract()

