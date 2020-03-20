'''
File: TrigalClick.py
Author: Minpto Kim
Projrct: WebCrawling
Description:
    Inclouds all of the function that finds and click element
'''
# coding: utf-8
from Connect import driver

'''
Function: clickCategory
Author: Minpto Kim
Description: 
    Finds element ID of the category and click found category that can
    acess option it needed
Input:
    index - Targetted category element ID number
'''
def clickCategory(index):
    # Name of the element ID
    strTmp = 'ctl00_body_dlApplication_ctl0' + str(index) + '_HyperLink1'
    tmp = driver.find_element_by_id(strTmp)
    tmp.click()


'''
Function: clickOption
Author: Minpto Kim
Description: 
    Finds element ID of the category and click found category that can
    acess option it needed
Input: 
    optionName - Name of the oprion inthe drop down menu
    optionVal - Vlaue of the drop down menu that what to click
'''
def clickOption(optionName, optionVal):
    strTmp = "//select[@id='ctl00_body_ddl" + optionName + "']/option["
    strTmp = strTmp + str(optionVal) + "]"
    optionSection = driver.find_element_by_xpath(strTmp)
    optionSection.click()
