# -*- coding:utf-8 -*-
# Author: Neng Qi\
#https://www.jianshu.com/p/2263d023b559
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expect


def startBrowser():
    browser = webdriver.Chrome(executable_path="G:/bootTemplate/chromedriver.exe")
    browser.get('http://www.baidu.com/')
    kw = browser.find_element_by_id("kw")
    kw.send_keys("Selenium", Keys.RETURN)

def startBrowser1():
    browser = webdriver.Chrome(executable_path="G:/bootTemplate/chromedriver.exe")
    browser.get('http://www.baidu.com/')
    kw = browser.find_element_by_id("kw")
    su = browser.find_element_by_id("su")
    kw.send_keys("Selenium")
    su.click()
def startBrowser2():
    browser = webdriver.Chrome(executable_path="G:/bootTemplate/chromedriver.exe")
    browser.get('http://www.baidu.com/')
    kw = browser.find_element_by_id("kw")
    kw.send_keys("Selenium")
    kw.submit()
    results = browser.find_elements_by_css_selector("#content_left .c-container")
    for result in results:
        link = result.find_element_by_xpath(".//h3/a")
        print(link.text)


def startBrowser3():
    browser = webdriver.Chrome(executable_path="G:/bootTemplate/chromedriver.exe")
    browser.get('http://www.baidu.com/')
    browser.execute_script(''' var kw = document.getElementById('kw');
    　　var su = document.getElementById('su');
    　　kw.value = 'Selenium';
    　　su.click();
    　　''')

def waitResult():
    browser = webdriver.Chrome(executable_path="G:/bootTemplate/chromedriver.exe")
    browser.get('http://www.tuniu.com/flight/intel/sha-sel')
    Wait(browser, 60).until(
        Expect.text_to_be_present_in_element((By.ID, "loadingStatus"), u"共搜索")
    )
    flight_items = browser.find_elements_by_class_name("flight-item")
    for flight_item in flight_items:
        flight_price_row = flight_item.find_element_by_class_name("flight-price-row")
        print(flight_price_row.get_attribute("data-no"))

if __name__ == '__main__':
    waitResult()
