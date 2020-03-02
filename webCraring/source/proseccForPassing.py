from guiGet import loopNum
from guiGet import getNameOption
from guiSetting import setSubOption
from dataClass import dataClass
from dataSetting import numOpOne
from dataSetting import numOpTwo
from dataSetting import numOpThree
from dataPreOut import numOpPrint


def loopingOne(mainMenuName, option1):
    lTmp = []
    data = dataClass()
    count = 0

    for i in range(2, loopNum(option1) + 1):
        setSubOption(option1, i)
        op1Name = getNameOption(option1, i)
        data = numOpOne(mainMenuName, op1Name)
        lTmp.append(data)
        numOpPrint(lTmp, count, 2)
        count = count + 1
    return lTmp


def loopingTwo(mainMenuName, option1, option2):
    lTmp = []
    data = dataClass()
    count = 0

    for i in range(2, loopNum(option1) + 1):
        setSubOption(option1, i)
        op1Name = getNameOption(option1, i)
        for j in range(2, loopNum(option2) + 1):
            setSubOption(option2, j)
            op2Name = getNameOption(option2, j)
            data = numOpTwo(mainMenuName, op1Name, op2Name)
            lTmp.append(data)
            numOpPrint(lTmp, count, 2)
            count = count + 1
    return lTmp


def loopingThree(mainMenuName, option1, option2, option3):
    lTmp = []
    data = dataClass()
    count = 0

    for i in range(2, loopNum(option1) + 1):
        setSubOption(option1, i)
        op1Name = getNameOption(option1, i)
        for j in range(2, loopNum(option2) + 1):
            setSubOption(option2, j)
            op2Name = getNameOption(option2, j)
            for k in range(2, loopNum(option3) + 1):
                setSubOption(option3, k)
                op3Name = getNameOption(option3, k)
                data = numOpThree(mainMenuName, op1Name, op2Name, op3Name)
                lTmp.append(data)
                numOpPrint(lTmp, count, 3)
                count = count + 1
    return lTmp
