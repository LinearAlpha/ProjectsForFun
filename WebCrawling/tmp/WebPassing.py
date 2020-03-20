from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Connect import driver
from ClickWeb import choiseOption
from WebData import numElement
from WebData import optionName
from SettingData import numOpOne
from SettingData import numOpTwo
from SettingData import numOpThree
from DataProcess import optionPrint
from DataClass import dataClass

"""
Function: webLoadCheck
Author: Minpto Kim
Description: This function checks the webpage loaded element that has
             class name as "product-name"
Input: N/A
Output: True; the webpage loaded with element that is looking for
        False; the webpage dose not have element that is looking for
"""
def webLoadCheck():
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-name")))
    except Exception:
        return False
    return True


"""
Function: oneOprionChoicse
Author: Minpto Kim
Description: Case for the only one drop down menu
Input: categoryName; name of the category in the webpage
       option1; name of the option thayt activaited
Output: tmp; store class of the data thay contains informations of the webpage
"""
def oneOprionChoicse(categoryName, option1):
    tmp = []
    count = 0
    # skip the fist elemtn and looping until the last selection of the second
    # option
    for i in range(2, numElement(option1)):
        # define the class for the data storage
        choiseOption(option1, i)
        # The webpage loaded with element that we are looking for
        if webLoadCheck():
            op1Name = optionName(categoryName, i)
            data = dataClass()
            data = numOpOne(option1, op1Name)
            tmp.append(data)
            optionPrint(tmp, count, 2)
            count = count + 1
    return tmp


"""
Function: twoOprionChoicse
Author: Minpto Kim
Description: Case for the two drop down menu
Input: categoryName; name of the category in the webpage
       option1; name of the option thayt activaited
       option2; name of the option thayt activaited
Output: tmp; store class of the data thay contains informations of the webpage
"""
def twoOprionChoicse(categoryName, option1, option2):
    tmp = []
    count = 0
    # skip the fist elemtn and looping until the last selection of the second
    # option for the all other loop
    for i in range(2, numElement(option1)):
        choiseOption(option1, i)
        op1Name = optionName(categoryName, i)
        for j in range(2, numElement(option2)):
            choiseOption(option2, j)
            if webLoadCheck():
                op2Name = optionName(option2, j)
                data = dataClass()
                data = numOpTwo(categoryName, op1Name, op2Name)
                tmp.append(data)
                optionPrint(tmp, count, 2)
                count = count + 1
    return tmp


"""
Function: threeOprionChoicse
Author: Minpto Kim
Description: Case for the three drop down menu
Input: categoryName; name of the category in the webpage
       option1; name of the option thayt activaited
       option2; name of the option thayt activaited
       option3; name of the option thayt activaited
Output: tmp; store class of the data thay contains informations of the webpage
"""
def threeOprionChoicse(categoryName, option1, option2, option3):
    tmp = []
    count = 0
    # skip the fist elemtn and looping until the last selection of the second
    # option for the all other loop
    for i in range(2, numElement(option1)):
        choiseOption(option1, i)
        op1Name = optionName(categoryName, i)
        for j in range(2, numElement(option2)):
            choiseOption(option2, j)
            op2Name = optionName(categoryName, j)
            for k in range(2, numElement(option3)):
                choiseOption(option3, k)
                if webLoadCheck():
                    op3Name = optionName(categoryName, k)
                    data = dataClass()
                    data = numOpThree(categoryName, op1Name, op2Name, op3Name)
                    tmp.append(data)
                    optionPrint(tmp, count, 2)
                    count = count + 1
    return tmp
