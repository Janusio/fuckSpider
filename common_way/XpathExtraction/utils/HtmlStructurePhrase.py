from bs4 import BeautifulSoup
import requests
from lxml import etree
import codecs
def getALlNode():
    url1="https://www.jianshu.com/p/48d6aae7dc8e"
    url2="http://www.cde.org.cn/transparent.do?method=spxlList&branchType=%E4%B8%93%E4%B8%9A&department=%E5%8C%96%E8%8D%AF%E4%B8%B4%E5%BA%8A%E4%B8%80%E9%83%A8&isTimetag=0&isZy=0&pageMaxNum=20&pageMaxNumber=20&tasktype=fb&currentPageNumber=1"

    r1=requests.get(url1)
    # r2=requests.get(url2)
    html1=r1.content.decode('utf-8')
    # html2=r2.content.decode('utf-8')
    # dom_tree = etree.HTML(html)
    soup1=BeautifulSoup(html1,"lxml")
    # soup2=BeautifulSoup(html2,"lxml")
    # for ell in soup1.children:
    #     print (len(ell))
    #
    for ee in soup1.descendants:
        if ee.name is not None:
            res=ee.name
            for parent in ee.parents:
                if parent is None:
                    res=ee.name+'//'
                else:
                    res=parent.name+"/"
            print(res)
    table=soup1.body
    for parent in table.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)
    res=""
    print(getpp(soup1.body.string,res))

def getpp(html,res):
    html_soup=BeautifulSoup(html,"lxml")
    if  html_soup.name is not None and html_soup.contents is None:
        res=html_soup.name
    elif html_soup.contents is not None:
        for eee in html_soup.children:
            if eee.name is not None and eee.string is not None:
                res+=getpp(eee.string,res)
    return res
if __name__ == '__main__':
    getALlNode()