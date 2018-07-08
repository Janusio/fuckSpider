from bs4 import BeautifulSoup
import requests
from lxml import etree
import codecs

listAll = []
listExceptName=["meta","script"]
listChoose=["id","class","name"]

def getALlNode(url1):
    url2 = "https://www.jianshu.com/p/48d6aae7dc8e"
    # url1 = "http://www.cde.org.cn/transparent.do?method=spxlList&branchType=%E4%B8%93%E4%B8%9A&department=%E5%8C%96%E8%8D%AF%E4%B8%B4%E5%BA%8A%E4%B8%80%E9%83%A8&isTimetag=0&isZy=0&pageMaxNum=20&pageMaxNumber=20&tasktype=fb&currentPageNumber=1"

    # r1 = requests.get(url1)
    # html1 = r1.content.decode('utf-8')
    # soup1 = BeautifulSoup(html1, "lxml")
    # soup2 = BeautifulSoup(open(url1),"lxml",from_encoding='gbk')
    soup1 = BeautifulSoup(codecs.open(url1, 'r', encoding='utf-8'), 'lxml')
    # print(type(soup1.head))
    # print(soup1.head)
    # print(soup1.head.title)
    # print(soup1.head.string)
    # for i in soup1.html.children:
    #     print(i)
    #     print('-------------------')
    printHtml(soup1.html)


def printHtml(soup1):
    if soup1.name is not None and soup1.children is not None:
        for iii in soup1.children:
            if iii.name is not None and iii.name not in listExceptName :

                # print('-------------------')
                # print(iii.name)
                res = "/"+iii.name
                if len(iii.attrs) != 0:
                    # print(iii.attrs)
                    for key, value in iii.attrs.items():
                        if key in listChoose:
                            if key == "class":
                                res =res+ ("[@{}=\"{}\"]".format(key, value[0]) )
                                continue
                            else:
                                res =res+ ("[@{}=\"{}\"]".format(key, value) )
                                continue

                for parent in iii.parents:
                    if parent is None:
                        res = iii.name + '//'
                        # print(res)
                    else:
                        res += ( "/"+parent.name )
                        if len(parent.attrs) != 0:
                            # print(iii.attrs)
                            for key,value in parent.attrs.items():
                                if key in listChoose:
                                    if key=="class":
                                        res = res + ("[@{}=\"{}\"]".format(key,value[0]))
                                        continue
                                    else:
                                        res = res + ( "[@{}=\"{}\"]".format(key, value))
                                        continue
                        # print(res)
                listAll.append(res)
            printHtml(iii)
                # print(res)
    else:
        if soup1.name is not None and soup1.name not in listExceptName:

            # print('-------------------')
            # print(iii.name)
            res = soup1.name + '/'
            for parent in soup1.parents:
                if parent is None:
                    res = soup1.name + '//'
                    # print(res)
                else:
                    if len(parent.attrs) != 0:
                        # print(iii.attrs)
                        for key, value in parent.attrs.items():
                            if key in listChoose:
                                if key == "class":
                                    res += ("[@{}=\"{}\"]".format(key, value[0]) + "/")
                                    continue
                                else:
                                    res += ("[@{}=\"{}\"]".format(key, value) + "/")
                                    continue
                    else:
                        res += (parent.name + "/")
                        # print(res)
            listAll.append(res)


def dealTheStringToXpath(tempStr):
    temp = 'td/tr/tbody/table/td/tr/table/form/body/html/[document]/'
    tempGroup = tempStr.split('/')
    groupGroup = tempGroup[1:len(tempGroup) - 1]
    groupGroup.reverse()
    xpathRes = ""
    for ii in groupGroup:
        xpathRes += ('/' + ii)
    # print(xpathRes)
    return xpathRes
    # print(groupGroup)


def funMainList(url):
    getALlNode(url)
    # for per in listAll:
    #     print(per)
    listNoRe = list(set(listAll))
    listXpath = []
    for iii in listNoRe:
        # print('/html'+dealTheStringToXpath(iii))
        listXpath.append(dealTheStringToXpath(iii))
    listXpath.sort()
    return listXpath


    # print(len(listAll))
    # print(len(listNoRe))
    # dealTheStringToXpath()
if __name__ == '__main__':
    url="test1.html"
    funMainList(url)
    #     getALlNode()
    #     # for per in listAll:
    #     #     print(per)
    #     listNoRe = list(set(listAll))
    #     for iii in listNoRe:
    #         print(dealTheStringToXpath(iii))
    #     # print(len(listAll))
    #     print(len(listNoRe))
    #     # dealTheStringToXpath()
