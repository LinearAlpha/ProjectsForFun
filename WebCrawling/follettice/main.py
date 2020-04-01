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
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def accessWeb(url):
    driver.get(url)
    driver.implicitly_wait(5)
    print(driver.current_url)

def checkReasult():
    reasultOut = False
    try:
        assert "No resources found" in driver.page_source
        reasultOut = True
    except Exception:
        pass
    finally:
        return reasultOut

# Check what kinf of OS it is useing
sysName = platform.system()
tmp = '\n' "You are OS is " + sysName + '\n'
print(tmp)
# Acess chromedriver by the OS
if tmp == "Linux":
    tmp = os.path.dirname(os.path.realpath(__file__))
    tmp = tmp + "/ChromeDriver/lunx/chromedriver"
else:
    tmp = os.path.dirname(os.path.realpath(__file__))
    tmp = tmp + "\\ChromeDriver\\windows\\chromedriver"
# Opens the CSV file that has product information
f = open('tmp.csv', 'rt')
rdr = csv.reader(f)
data = []
# read each line to ans store as list
for line in rdr:
    data.append(line)
    print(line)
# close the fine that opened
f.close()
url = "https://www.follettice.com/sales-literature/model-number"
driver = webdriver.Firefox()
accessWeb(url)
j = 0
for i in range(1, len(data)):
    accessWeb("https://www.google.com")
    url = "https://www.follettice.com/sales-literature/model-number?combine="
    url = url + data[i][0]
    accessWeb(url)
    if checkReasult() == False:
        a = input("test: ")
a = input("End")








