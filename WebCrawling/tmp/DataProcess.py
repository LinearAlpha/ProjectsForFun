from dataClass import dataClass

def findAndReplase(Data):
    return Data.replace("Everpure ", "")

def productDataOut(tmp):
    




    z = 0
    tmp = []
    max = len(strTmp[0])
    if strTmp[0][0].find("System"):
        tmp.append(findAndReplase(strTmp[0][0], 1))
        tmp.append(strTmp[1][0])
        tmp.append("N/A")
        tmp.append("N/A")
        tmp.append("N/A")
    elif max == 2:
        for i in range(0, max):
            tmp.append(findAndReplase(strTmp[0][i], 1))
            tmp.append(strTmp[1][i])
            if i == max - 1:
                tmp.append(findAndReplase(strTmp[1][i], 2))
    else:
        tmp.append("N/A")
        tmp.append("N/A")
        tmp.append(findAndReplase(strTmp[0][z], 1))
        tmp.append(strTmp[1][z])
        tmp.append(findAndReplase(strTmp[2][z], 2))
    return tmp


def optionPrint(lTmp, count, option):
    strTmp = lTmp[count].getProductInfo()
    max = len(strTmp[0])
    if option == 1:
        for z in range(0, max):
            tmp = lTmp[count].getMainName() + "\t"
            tmp = tmp + lTmp[count].getoPtion1Name() + "\t"
            tmp = tmp + strTmp[0][z] + "\t"
            tmp = tmp + strTmp[1][z] + "\t"
            tmp = tmp + strTmp[2][z]
            print(tmp)
    elif option == 2:
        for z in range(0, max):
            tmp = lTmp[count].getMainName() + "\t"
            tmp = tmp + lTmp[count].getoPtion1Name() + "\t"
            tmp = tmp + lTmp[count].getoPtion2Nmae() + "\t"
            tmp = tmp + strTmp[0][z] + "\t"
            tmp = tmp + strTmp[1][z] + "\t"
            tmp = tmp + strTmp[2][z]
            print(tmp)
    elif option == 3:
        for z in range(0, max):
            tmp = lTmp[count].getMainName() + "\t"
            tmp = tmp + lTmp[count].getoPtion1Name() + "\t"
            tmp = tmp + lTmp[count].getoPtion2Nmae() + "\t"
            tmp = tmp + lTmp[count].getOption3Name() + "\t"
            tmp = tmp + strTmp[0][z] + "\t"
            tmp = tmp + strTmp[1][z] + "\t"
            tmp = tmp + strTmp[2][z]
            print(tmp)






def dataForSave(thewriter, allData, option):
    strTmp = allData.getProductInfo()
    tmp = []
    tmp.append(allData.getMainName())
    tmp.append(allData.getoPtion1Name())
    if option == 1:
        produCTmp = productOutSetting(strTmp)
    elif option == 2:
        tmp.append(allData.getoPtion2Nmae())
        produCTmp = productOutSetting(strTmp)
    elif option == 3:
        tmp.append(allData.getoPtion2Nmae())
        tmp.append(allData.getOption3Name())
        produCTmp = productOutSetting(strTmp)
    max = len(produCTmp)
    for i in range(0, max):
        tmp.append(produCTmp[i])
    thewriter.writerow(tmp)
