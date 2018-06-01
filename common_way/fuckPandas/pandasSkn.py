# -*- coding:utf-8 -*-
# Author: Neng Qi
from numpy.random import randn
def getRandomN():
    data={i:randn() for i in range(7)}
    print(data)


if __name__=='__main__':
    getRandomN()