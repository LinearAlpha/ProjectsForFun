from connect import driver


def getNameMainMenu(index):
    strTmp = 'ctl00_body_dlApplication_ctl0' + str(index) + '_HyperLink1'
    tmp = driver.find_element_by_id(strTmp)
    tmp.click()


def getNameManufacturer(ManufacturerVal):
    strTmp = "//option[@value='" + str(ManufacturerVal) + "']"
    Manufacturer = driver.find_element_by_xpath(strTmp)
    ManufacturerName = Manufacturer.text
    return ManufacturerName


def getNameModel(modelVal):
    model = driver.find_element_by_xpath(
        "//option[@value='" + str(modelVal) + "']")
    model.click()
