'''
File: Main.py
Author: Minpto Kim
Projrct: WebCrawling
Project Description:
    Acess indiviual options on the everpuresizing.com ans store as an excel
    file
Description:
    It is setting and calling function for Crawling    
'''
#coding: utf-8
import csv
import os
from WebScraping import captureCategory
from WebScraping import clickCategory
from WebScraping import numOptionOne
from WebScraping import numOptionTwo
from WebScraping import numOptionThree

# The list thay will going to store data class
allData = []

# Coffe
i = 0
clickCategory(i)
categoryName = captureCategory(i)
# Name of the elemrnt ID
option1 = "Manufacturer"
option2 = "Model"
tmp = numOptionTwo(categoryName, option1, option2)
allData.append(tmp)

i = 2
clickCategory(i)
categoryName = captureCategory
option1 = "Espresso"