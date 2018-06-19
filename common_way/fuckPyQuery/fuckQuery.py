from pyquery import PyQuery as pq
from lxml import etree
import requests
def getMainSource():
    # v_source=pq("")
    # //直接加载一个html串
    # v_source = pq("")
   # - --加载位于指定路径下的html文件
   #  v_source = pq(filename=path_to_html_file)
    # - --加载url地址直接进行解析
    url="http://yunvs.com/list/mai_1.html"
    # v_source = pq(url=url)
    r=requests.get(url)
    v_source = pq(r)
    for data in v_source('tr'):
        print(pq(data).html())
if __name__ == '__main__':
    getMainSource()
