from Connect import driver
from DataClass import dataClass as DC

def getCategory(index):
    tmp = 'ctl00_body_dlApplication_ctl0' + str(index) + '_HyperLink1'
    tmp = driver.find_element_by_id(tmp)
    return tmp.text

def numElement(optionName):
    tmp = "//select[@id='ctl00_body_ddl" + optionName + "']"
    tmp = driver.find_element_by_xpath(tmp)
    return tmp.text.count('\n')

def optionName(optionName, optionVal):
    tmp = "//select[@id='ctl00_body_ddl" + optionName + "']/option["
    tmp = tmp + str(optionVal) + "]"
    tmp = driver.find_element_by_xpath(tmp)
    return tmp.text

def producName():
    lTmp = []
    tmp = "product-name"
    tmp = driver.find_elements_by_class_name(tmp)
    for i in range(0, len(tmp)):
        lTmp.append(tmp[i].text)
    return lTmp

def producPrice(max):
    lTmp = []
    for i in range(0, max):
        tmp = "ctl00_body_ResultList_ctl0" + str(i) + "_lblPrice"
        tmp = driver.find_element_by_id(tmp)
        lTmp.append(tmp.text)
    return lTmp


def producBenefit(max):
    lTmp = []
    for i in range(0, max):
        tmp = "ctl00_body_ResultList_ctl0" + str(i) + "_lblSysBenefits"
        tmp = driver.find_element_by_id(tmp)
        tmp = tmp.find_elements_by_tag_name("li")
        lTmp.append(tmp[0].text)
    return lTmp
