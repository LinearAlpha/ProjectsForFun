'''
File: Connect.py
Author: Minpto Kim
Projrct: WebCrawling
Description:
    It opends chrome browser abd acess everpure webpage for Crawling
    to run this it must needed chromedriver.exe
'''
#coding: utf-8
from selenium import webdriver

# ChromeDriver if it not work check driver version
driver = webdriver.Chrome()
# Everpure sizig link
driver.get('http://www.everpuresizing.com/')
driver.implicitly_wait(5)
# Print current URL
print(driver.current_url)