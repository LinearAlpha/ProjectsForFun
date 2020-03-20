from dataClass import dataClass
from WebData import producName
from WebData import producPrice
from WebData import producBenefit


def numOpOne(categoryName, op1Name):
    data = dataClass()
    tmp = []
    data.setMainName(categoryName)
    data.setOption1Name(op1Name)
    data.setNumLoop(1)
    tmp.append(producName())
    max = len(tmp[0])
    tmp.append(producPrice(max))
    tmp.append(producBenefit(max))
    data.setProductInfo(tmp)
    return data

def numOpTwo(categoryName, op1Name, op2Name):
    data = dataClass()
    tmp = []
    data.setMainName(categoryName)
    data.setOption1Name(op1Name)
    data.setOption2Name(op2Name)
    data.setNumLoop(2)
    tmp.append(producName())
    max = len(tmp[0])
    tmp.append(producPrice(max))
    tmp.append(producBenefit(max))
    data.setProductInfo(tmp)
    return data


def numOpThree(categoryName, op1Name, op2Name, op3Name):
    data = dataClass()
    tmp = []
    data.setMainName(categoryName)
    data.setOption1Name(op1Name)
    data.setOption2Name(op2Name)
    data.setOption3Name(op3Name)
    data.setNumLoop(2)
    tmp.append(producName())
    max = len(tmp[0])
    tmp.append(producPrice(max))
    tmp.append(producBenefit(max))
    data.setProductInfo(tmp)
    return data
