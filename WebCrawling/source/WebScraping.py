'''
File: WebScraping.py
Author: Minpto Kim
Projrct: WebCrawling
Description:
    Functions for scraping    
'''
# coding: utf-8
from DataCapturing import numElement
from DataCapturing import menuName
from DataCapturing import captureCategory
from TrigalClick import clickCategory
from TrigalClick import clickOption
from DataStore import numOptionOneData
from DataStore import numOptionTwoData
from DataStore import numOptionThreeData


def menuValidation(optionName, optionVal):
    if menuName(optionName, optionVal) == "select one..":
        return False
    else:
        return True


def numOptionOne(category, option1):
    # Holinding list of data class before return it
    data = []
    for i in range(1, numElement(option1) + 1):
        clickOption(option1, i)
        if menuValidation(option1, i):
            tmp = numOptionOneData(category, option1, i)
            data.append(tmp)
    return data


def numOptionTwo(category, option1, option2):
    data = []
    for i in range(1, numElement(option1) + 1):
        clickOption(option1, i)
        if menuValidation(option1, i):
            for j in range(1, numElement(option2) + 1):
                clickOption(option2, j)
                if menuValidation(option2, j):
                    tmp = numOptionTwoData(category, option1, option2, i, j)
                    data.append(tmp)
    return data

def numOptionThree(category, option1, option2, option3):
    data = []
    for i in range(1, numElement(option1) + 1):
        clickOption(option1, i)
        if menuValidation(option1, i):
            for j in range(1, numElement(option2) + 1):
                clickOption(option2, j)
                if menuValidation(option2, j):
                    for k in range(1, numElement(option3) + 1):
                        if menuValidation(option3, k):
                            tmp = numOptionThreeData(
                                category, option1, option2, option3, i, j, k)
                            data.append(tmp)
    return data
                            
                            
                            
                            
        
                            
                            
                            
                            
                            
                            
                            
                            
                            
                