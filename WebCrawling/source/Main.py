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
from Connect import clsoeWeb
from WebScraping import captureCategory
from WebScraping import clickCategory
from WebScraping import numOptionOne
from WebScraping import numOptionTwo
from WebScraping import numOptionThree
from IceSpetialCase import byManifactura


def callingFnc(numLocalOp, i, option1, option2, option3):
    clickCategory(i)
    if numLocalOp == 1:
        allData.append(numOptionOne(captureCategory(i), option1))
    elif numLocalOp == 2:
        allData.append(numOptionTwo(captureCategory(i), option1, option2))
    elif numLocalOp == 3:
        allData.append(numOptionThree(
            captureCategory(i), option1, option2, option3))

# Change the workinf directory for saving
os.chdir("..")
if os.path.isdir("Data"):
    os.chdir("Data")
else:
    os.makedirs("Data")
    os.chdir("Data")
print("\nYour reasult will be goin to saved on\n")
tmp = os.getcwd() + '\n'
print(tmp)

# The list thay will going to store data class
allData = []
# Name of the elemrnt ID
option1 = ""
option2 = ""
option3 = ""

# # Coffe
# i = 0
# option1 = "Manufacturer"
# option2 = "Model"
# callingFnc(2, i, option1, option2, option3)

# # Espresso
# i = 1
# option1 = "Espresso"
# callingFnc(1, i, option1, option2, option3)

# Fountain
i = 2
option1 = "FountainDrink"
option2 = "CarbonatorType"
option3 = "CarbonatorNo"
callingFnc(3, i, option1, option2, option3)

# Frozen Carbonated Beverage
i = 3
option1 = "Manufacturer"
option2 = "Model"
callingFnc(2, i, option1, option2, option3)

# Hot Water Dispensing
i = 4
option1 = "Manufacturer"
option2 = "Model"
callingFnc(2, i, option1, option2, option3)

# Ice
i = 5
option1 = "IceNumber"
option2 = "IceWeightType"
option3 = "IceWeightPounds"
clickCategory(i)
iceDATA = []
iceDATA.append(byManifactura(captureCategory(i)))
iceDATA.append(byManifactura(captureCategory(i)))

# Iced Tea
i = 6
option1 = "Manufacturer"
option2 = "Model"
callingFnc(2, i, option1, option2, option3)

# Specialty Beverage
i = 7
option1 = "Manufacturer"
option2 = "Equipment"
option3 = "Model"
callingFnc(3, i, option1, option2, option3)

# Steam Oven
i = 8
option1 = "Manufacturer"
option2 = "Model"
callingFnc(2, i, option1, option2, option3)

# Whole Store
i = 9
option1 = "Carbonators"
option2 = "DailyProduction"
option3 = "brewer"
callingFnc(3, i, option1, option2, option3)
