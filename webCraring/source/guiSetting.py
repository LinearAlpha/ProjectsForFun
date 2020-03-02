from connect import driver


def setMainMenu(index):
    strTmp = 'ctl00_body_dlApplication_ctl0' + str(index) + '_HyperLink1'
    tmp = driver.find_element_by_id(strTmp)
    tmp.click()


def setSubOption(optionName, optionVal):
    strTmp = "//select[@id='ctl00_body_ddl" + \
        optionName + "']/option[" + str(optionVal) + "]"
    optionSection = driver.find_element_by_xpath(strTmp)
    optionSection.click()
