# -*- coding:utf-8 -*-
import json


def readFile():
    path = "example.txt"
    print(open(path).readline())

def readFile1():

    path = "example.txt"
    records=[json.loads(line) for line in open(path)]
    print(records[0])


if __name__ == '__main__':
    readFile1()
