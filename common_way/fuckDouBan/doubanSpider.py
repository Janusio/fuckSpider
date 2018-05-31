# -*- coding: utf-8 -*-
import requests
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