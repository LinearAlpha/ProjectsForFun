# coding: utf-8
from WebDataClass import webData as WD
from DataCapturing import menuName
from DataCapturing import producName
from DataCapturing import price
from DataCapturing import producBenefit

def producInformation():
    tmp = []
    tmp.append(producName())
    max = len(tmp[0])
    tmp.append(price(max))
    tmp.append(producBenefit(max))
    return tmp 

def numOptionOneData(category, option1, index):
    data = WD()
    data.setCategory(category)
    data.setNumOption(1)
    data.setOptionOne(menuName(option1, index))
    data.setProductInfo(producInformation())
    return data

def numOptionTwoData(category, option1, option2, i, j):
    data = WD()
    data.setCategory(category)
    data.setNumOption(2)
    data.setOptionOne(menuName(option1, i))
    data.setOptionTwo(menuName(option2, j))
    data.setProductInfo(producInformation())
    return data
    
def numOptionThreeData(category, option1, option2, option3, i, j, k):
    data = WD()
    data.setCategory(category)
    data.setNumOption(3)
    data.setOptionOne(menuName(option1, i))
    data.setOptionTwo(menuName(option2, j))
    data.setOptionThree(menuName(option3, k))
    data.setProductInfo(producInformation())
    return data
    
    
def findREplase (tmp):
    tmp.replace("Everpure ", "")
    return tmp
    
def saveData(wr, data):
    for i in range(0, len(data)):
        tmp = data[i].getProductInfo()
        max = len(tmp[0])
        dataOut = []
        dataOut.append(data[i].setCategory())
        for j in range(0, max):
            dataOut.append(findREplase(tmp[0][j]))
            dataOut.append(tmp[2][j])
            
        