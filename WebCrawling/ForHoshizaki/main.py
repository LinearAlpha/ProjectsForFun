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
from selenium import webdriver

def accessWeb(url):
    driver.get(url)
    driver.implicitly_wait(10)
    print(driver.current_url)

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
# Open the Chrome and imort Chrome driver
driver = webdriver.Chrome(tmp)
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
dataout = []
# Check indiviaul webpage that has producinformation
print(len(data))
for i in range(0, len(data)):
    tmp = data[i][0].replace("*", "")
    url = "https://www.hoshizakiamerica.com/product/" + tmp
    # Redirect the webpage for the produc information
    accessWeb(url)
    xpathTmp = '//h2[@class="product_title entry-title"]'
    preOut = []
    # If product name is not loaded, pass it
    try:
        webInfo = driver.find_element_by_xpath(xpathTmp)
        webText = webInfo.text
        # Check is there same produc name on the webpage
        if webText.find(tmp) != -1:
            preOut.append(tmp)
            preOut.append("V")
            preOut.append(webText)
            preOut.append(driver.current_url)
            dataout.append(preOut)
        else:
            preOut.append(tmp)
            preOut.append("X")
            preOut.append("N/A")
            preOut.append("N/A")
            dataout.append(preOut)
    except Exception:
        preOut.append(tmp)
        preOut.append("X")
        preOut.append("N/A")
        preOut.append("N/A")
        dataout.append(preOut)
        pass
    print(preOut)
# Close the Chrome
driver.close()
# Open or create file to write data collected on the web
f = open('outTMP.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerows(dataout)
# Close the file
f.close()
# Open or create file to write data collected on the web
f = open('out.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
for i in range(0, len(dataout)):
    wr.writerow(dataout[i])
# Close the file
f.close()