from utils.TransferToXpathList import funMainList
import requests
from lxml import etree
import codecs
import json


def inMultiUrl(url1, url2):
    listUrl1 = funMainList(url1)
    print(len(listUrl1))
    listUrl2 = funMainList(url2)
    print(len(listUrl2))
    for per1, per2 in zip(listUrl1, listUrl2):
        if per1 != per2:
            print('{},{}'.format(per1, per2))
        else:
            print("OK!")


def inXpathDif(url1, url2):
    listUrl1 = funMainList(url1)
    listUrl2 = funMainList(url2)
    # r1 = requests.get(url1)
    # r2 = requests.get(url2)
    # html1 = r1.content.decode('utf-8')
    # html2 = r2.content.decode('utf-8')
    # html1=open(url1)
    f = open('test1.html', 'r', encoding="utf-8")
    html1 = f.read()
    # print (html)
    f.close()
    # html2=open(url2)
    dom_tree1 = etree.HTML(html1)
    dom_tree2 = etree.HTML(html1)
    # dom_tree1=etree.ElementTree(file=url1)
    # dom_tree2=etree.ElementTree(file=url2)
    dictRes = {}
    for per1, per2 in zip(listUrl1, listUrl2):
        perXml1 = dom_tree1.xpath(per1)
        perXml2 = dom_tree2.xpath(per2)
        # print('{},{}'.format(perXml1, perXml2))
        for perContents1, perContents2 in zip(perXml1, perXml2):

            # print('{},{}'.format(perContents1.xpath('text()'), perContents2.xpath('text()')))
            if perContents1.xpath('text()') == perContents2.xpath('text()'):
                dictRes[per1.split('/')[len(per1.split()) - 2]] = per1
    jsonRes = json.dumps(dictRes, sort_keys=True, indent=4, separators=(',', ': '))
    print(jsonRes)


if __name__ == '__main__':
    # url1 = "http://www.cde.org.cn/transparent.do?method=spxlList&branchType=%E4%B8%93%E4%B8%9A&department=%E5%8C%96%E8%8D%AF%E4%B8%B4%E5%BA%8A%E4%B8%80%E9%83%A8&isTimetag=0&isZy=0&pageMaxNum=20&pageMaxNumber=20&tasktype=fb&currentPageNumber=1"
    # url2 = "http://www.cde.org.cn/transparent.do?method=spxlList&branchType=%E4%B8%93%E4%B8%9A&department=%E5%8C%96%E8%8D%AF%E4%B8%B4%E5%BA%8A%E4%BA%8C%E9%83%A8&isTimetag=0&isZy=0&pageMaxNum=20&pageMaxNumber=20&tasktype=fb&currentPageNumber=1"
    # url1='http://samr.cfda.gov.cn/WS01/CL0778/226286.html'
    # url2='http://samr.cfda.gov.cn/WS01/CL0779/225546.html'
    # inMultiUrl(url1,url2)
    url1="test1.html"
    url2="test1.html"
    inXpathDif(url1, url2)
