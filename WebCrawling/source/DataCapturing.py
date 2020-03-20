'''
File: DataCapturing.py
Author: Minpto Kim
Projrct: WebCrawling
Description:
    Get nessery data form the webpage    
'''
#coding: utf-8
from Connect import driver

'''
Function: captureCategory
Author: Minpto Kim
Description:
    Find the text of the element, and return as string
Input:
    int index - Targetted category element ID number
OutPut:
    string tmp - Text value of the element
'''
def captureCategory(index):
    # Name of the element ID
    strTmp = 'ctl00_body_dlApplication_ctl0' + str(index) + '_HyperLink1'
    tmp = driver.find_element_by_id(strTmp)
    # Return text of the element
    strTmp = tmp.text()
    return strTmp

'''
Function: numElement
Author: Minpto Kim
Description:
    Access the drop down menu of the element and return number of the index
Input:
    string optionName - Targetted drop down menu element ID name
OutPut:
    int tmp - Number of the element in the drop down menu
'''
def numElement(optionName):
    # Name of the element ID by the ID
    strTmp = 'ctl00_body_ddl' + optionName
    tmp = driver.find_element_by_id(strTmp)
    # Find nuber of enter in the string and return the amount of it
    return tmp.text.count('\n')

'''
Function: menuName
Author: Minpto Kim
Description:
    Access the drop down menu of the element and return text on the index
Input:
    string optionName - Targetted drop down menu element ID name
    int optionVal - Targetted drop down index
OutPut:
    string tmp - Text value of the element
'''
def menuName(optionName, optionVal):
    # Name of the element ID and location of the index
    strTmp = "//select[@id='ctl00_body_ddl" + optionName + "']/option["
    strTmp = strTmp + str(optionVal) + "]"
    tmp = driver.find_element_by_xpath(strTmp)
    # Find the text of the index and return it
    return tmp.text

'''
Function: producName
Author: Minpto Kim
Description:
    Find all of the product information element and return text value of the 
    the elemt
Input:
    N/A
OutPut:
    string lTmp - Text value of the element
'''
def producName():
    # List of string data from the web
    lTmp = []
    # Find and access product name element
    tmp = driver.find_elements_by_class_name("product-name")
    for i in range(0, len(tmp)):
        lTmp.append(tmp[i].text)
    return lTmp

'''
Function: price
Author: Minpto Kim
Description:
    Find all of the product price information of the element and return text
    value of the element
Input:
    int max - limit of the loop
OutPut:
    string lTmp - Text value of the element
'''
def price(max):
    # List of string data from the web
    lTmp = []
    for i in range(0, max):
        # Find and access indiviaul price information
        strTmp = "ctl00_body_ResultList_ctl0" + str(i) + "_lblPrice"
        tmp = driver.find_element_by_id(strTmp)
        lTmp.append(tmp.text)
    return lTmp

'''
Function: price
Author: Minpto Kim
Description:
    Find all of the product benefit information of the element and return text
    value of the element
Input:
    int max - limit of the loop
OutPut:
    string lTmp - Text value of the element
'''
def producBenefit(max):
    # List of string data from the web
    lTmp = []
    for i in range(0, max):
        strTmp = "ctl00_body_ResultList_ctl0" + str(i) + "_lblSysBenefits"
        tmp = driver.find_element_by_id(strTmp)
        tmp = tmp.find_elements_by_tag_name("li")
        lTmp.append(tmp[0].text)
    return lTmp