from dataClass import dataClass
from guiGet import getProducName
from guiGet import getProducPrice
from guiGet import getProducBenefit


def numOpOne(mainMenuName, op1Name):
    data = dataClass()
    strTmp = []
    data.setMainName(mainMenuName)
    data.setOption1Name(op1Name)
    data.setNumLoop(1)
    strTmp.append(getProducName())
    max = len(strTmp[0])
    strTmp.append(getProducPrice(max))
    strTmp.append(getProducBenefit(max))
    for k in range(0, max + 1):
        data.setProductInfo(strTmp[k])
    return data


def numOpTwo(mainMenuName, op1Name, op2Name):
    data = dataClass()
    data.setMainName(mainMenuName)
    data.setOption1Name(op1Name)
    data.setOption2Name(op2Name)
    data.setNumLoop(2)
    strTmp = []
    strTmp.append(getProducName())
    max = len(strTmp[0])
    strTmp.append(getProducPrice(max))
    strTmp.append(getProducBenefit(max))
    for k in range(0, max + 1):
        data.setProductInfo(strTmp[k])
    return data


def numOpThree(mainMenuName, op1Name, op2Name, op3Name):
    data = dataClass()
    data.setMainName(mainMenuName)
    data.setOption1Name(op1Name)
    data.setOption2Name(op2Name)
    data.setOption3Name(op3Name)
    data.setNumLoop(3)
    strTmp = []
    strTmp.append(getProducName())
    max = len(strTmp[0])
    strTmp.append(getProducPrice(max))
    strTmp.append(getProducBenefit(max))
    for k in range(0, max + 1):

        data.setProductInfo(strTmp[k])
    return data
