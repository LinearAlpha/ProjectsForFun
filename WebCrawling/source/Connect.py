'''
File: Connect.py
Author: Minpto Kim
Projrct: WebCrawling
Description:
    It opends chrome browser abd acess everpure webpage for Crawling
    to run this it must needed chromedriver.exe
'''
#coding: utf-8
import os
import platform
from selenium import webdriver

def accessWeb(url):
    # Everpure sizig link
    driver.get('http://www.everpuresizing.com/')
    driver.implicitly_wait(5)
    # Print current URL
    print(driver.current_url)

def clsoeWeb():
    driver.quit()

sysName = platform.system()
tmp = '\n' "You are OS is " + sysName + '\n'
print(tmp)
if tmp == "Linux":
    tmp = os.path.dirname(os.path.realpath(__file__))
    tmp = tmp + "/ChromeDriver/lunx/chromedriver"
else:
    tmp = os.path.dirname(os.path.realpath(__file__))
    tmp = tmp + "\\ChromeDriver\\windows\\chromedriver"

# ChromeDriver if it not work check driver version
driver = webdriver.Chrome(tmp)
url = "http://www.everpuresizing.com/"
accessWeb(url)