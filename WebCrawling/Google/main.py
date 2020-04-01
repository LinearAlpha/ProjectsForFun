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
    reasultOut = True
    try:
        assert "did not match any documents" not in driver.page_source
        reasultOut = False
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
url = "https://www.manitowocice.com/search.aspx?searchtext=test+123&searchmode=allwords#Site-Search"
driver = webdriver.Firefox()
accessWeb(url)

j = 0
for i in range(0, len(data)):
    url = "https://www.manitowocice.com/search.aspx?searchtext=" + data[i][0] + "&searchmode=allwords"    
    accessWeb(url)

    # webInfo = driver.find_element_by_name("q")
    # webInfo.clear()
    # webInfo.send_keys(search)
    # webInfo.submit()
    a = input("test: ")

a = input("End")








