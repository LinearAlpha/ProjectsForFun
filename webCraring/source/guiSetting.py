from connect import driver


def setMainMenu(index):
    strTmp = 'ctl00_body_dlApplication_ctl0' + str(index) + '_HyperLink1'
    tmp = driver.find_element_by_id(strTmp)
    tmp.click()


def setManufacturer(ManufacturerVal):
    strTmpID = "//select[@id='ctl00_body_ddlManufacturer']"
    strTmpVal = "//option[@value='" + str(ManufacturerVal) + "']"
    try:
        Manufacturer = driver.find_element_by_xpath(strTmpID).find_element_by_xpath(strTmpVal)
        Manufacturer.click()
    except Exception:
        pass
