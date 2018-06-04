# -*- coding:utf-8 -*-
# Author: Neng Qi
# https://www.jianshu.com/p/047d8c1c7e14
import numpy as  np
import time
import pandas as  pd
from pandas import Series, DataFrame

def getRandomN():
    data = {i: np.random.randn() for i in range(7)}
    print(data)


def testNumpr():
    my_arr = np.arange(1000000)
    my_list = list(range(1000000))
    start = time.time()
    for _ in range(10): my_arr2 = my_arr * 2
    end = time.time()
    print( end-start)

    start1 = time.time()
    for _ in range(10): my_list2 = [x * 2 for x in my_list]
    end1 = time.time()
    print(end1-start1 )

def testNumpyNdarray():
    data=np.random.rand(2,3)
    print(data)
    print(data*10)
    print(data+data)
    print(data+1)
def testPandasSeries():
    ob=pd.Series([1,2,3,4],index=['s','t','y','u'])
    # print(ob.values)
    print(ob)
if __name__ == '__main__':
    # getRandomN()
    # testNumpr()
    # testNumpyNdarray()
    testPandasSeries()