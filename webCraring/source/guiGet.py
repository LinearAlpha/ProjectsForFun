from connect import driver
import dataClass


def getNameMainMenu(index):
    strTmp = 'ctl00_body_dlApplication_ctl0' + str(index) + '_HyperLink1'
    tmp = driver.find_element_by_id(strTmp)
    trans = tmp.text
    return trans


def loopNum(optionName):
    strTmp = "//select[@id='ctl00_body_ddl" + optionName + "']"
    tmp = driver.find_element_by_xpath(strTmp)
    trans = tmp.text
    numOption = trans.count('\n')
    return numOption


def getNameOption(optionName, optionVal):
    strTmp = "//select[@id='ctl00_body_ddl" + \
        optionName + "']/option[" + str(optionVal) + "]"
    tmp = driver.find_element_by_xpath(strTmp)
    trans = tmp.text
    return trans


def getProducName():
    lTmp = []
    strTmp = "product-name"
    tmp = driver.find_elements_by_class_name(strTmp)
    max = len(tmp)
    for i in range(0, max):
        lTmp.append(tmp[i].text)
    return lTmp


def getProducPrice(max):
    lTmp = []
    for i in range(0, max):
        strTmp = "ctl00_body_ResultList_ctl0" + str(i) + "_lblPrice"
        tmp = driver.find_element_by_id(strTmp)
        lTmp.append(tmp.text)
    return lTmp


def getProducBenefit(max):
    lTmp = []
    for i in range(0, max):
        strTmp = "ctl00_body_ResultList_ctl0" + str(i) + "_lblSysBenefits"
        tmp = driver.find_element_by_id(strTmp)
        tmp = tmp.find_elements_by_tag_name("li")
        lTmp.append(tmp[0].text)
    return lTmp
