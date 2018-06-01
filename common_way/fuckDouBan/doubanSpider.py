# -*- coding: utf-8 -*-
import requests
# r.text 返回headers中的编码解析的结果，可以通过r.encoding = 'gbk'来变更解码方式
# r.content返回二进制结果
# r.json()返回JSON格式，可能抛出异常
# r.status_code
# r.raw返回原始socket respons，需要加参数stream=True
# session，自动保存cookies，可以设置请求参数，下次请求自动带上请求参数
#
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('http://httpbin.org/cookies')
#
# print(r.text)
# s = requests.Session()
# s.auth = ('user', 'pass') #权限认证
# s.headers.update({'x-test': 'true'})
# # both 'x-test' and 'x-test2' are sent
# s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# '{"cookies": {"sessioncookie": "123456789"}}'
# url = 'http://httpbin.org/post'
# >> > files = {'file': open('report.xls', 'rb')}
# >> > r = requests.post(url, files=files)
#
# 配置files，filename, content_type and headers
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
#
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
from lxml import etree
class Movie:
    def __init__(self,name,url,director,image_url):
        self.name=name
        self.director=director
        # self.actor=actor
        # self.publish_time=publish_time
        # self.area=area
        # self.type=type
        # self.score=score
        # self.count_comment=count_comment
        # self.good_comment=good_comment
        self.image_url=image_url
        self.url=url
    def toString(self):
        return self.name[0]+':'+self.director+':'+self.url[0]
def req_url():
    payload = {'start': '0', 'filter': ''}
    r=requests.get('https://movie.douban.com/top250',params=payload)
    html=r.content.decode('utf-8')
    dom_tree=etree.HTML(html)
    links=dom_tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
    movieList=[]
    for i in links:
        name=i.xpath('div[@class="item"]/div[1]/a[1]/img/@alt')
        url=i.xpath('div[@class="item"]/div[1]/a[1]/@href')
        image_url=i.xpath('div[@class="item"]/div[1]/a[1]/img/@src')
        info=i.xpath('div[1]/div[@class="info"]/div[2]/p[1]/text()')
        director=str(info).replace("&nbsp;",'').replace(' ','').split("主演")[0].replace('\n','').replace('\xa0','')
        movie=Movie(name,url,director,image_url)
        movieList.append(movie)
    # print(r.url)
    # print(r.text)
    return movieList
if __name__=='__main__':
    for i in req_url():
        print(i.toString())