from dataClass import dataClass
import csv


def numOpPrint(lTmp, count, option):
    strTmp = lTmp[count].getProductInfo()
    max = len(strTmp[0])
    if option == 1:

        for z in range(0, max):
            tmp = lTmp[count].getMainName() + "\t" + \
                lTmp[count].getoPtion1Name()
            tmp = tmp + "\t" + strTmp[0][z] + "\t" + \
                strTmp[1][z] + "\t" + strTmp[2][z]
            print(tmp)
    elif option == 2:
        for z in range(0, max):
            tmp = lTmp[count].getMainName(
            ) + "\t" + lTmp[count].getoPtion1Name() + "\t" + lTmp[count].getoPtion2Nmae()
            tmp = tmp + "\t" + strTmp[0][z] + "\t" + \
                strTmp[1][z] + "\t" + strTmp[2][z]
            print(tmp)
    elif option == 3:
        for z in range(0, max):
            tmp = lTmp[count].getMainName() + "\t" + lTmp[count].getoPtion1Name() + \
                "\t" + lTmp[count].getoPtion2Nmae() + "\t" + \
                lTmp[count].getOption3Name()
            tmp = tmp + strTmp[0][z] + "\t" + \
                strTmp[1][z] + "\t" + strTmp[2][z]
            print(tmp)


def dataForSave(thewriter, allData, option):
    strTmp = allData.getProductInfo()
    max = len(strTmp[0])
    if option == 1:
        for z in range(0, max):
            thewriter.writerow([allData.getMainName(), allData.getoPtion1Name(
            ), strTmp[0][z], strTmp[1][z], strTmp[2][z]])
    elif option == 2:
        for z in range(0, max):
            thewriter.writerow([allData.getMainName(), allData.getoPtion1Name(
            ), allData.getoPtion2Nmae(), strTmp[0][z], strTmp[1][z], strTmp[2][z]])
    elif option == 3:
        for z in range(0, max):
            thewriter.writerow([allData.getMainName(), allData.getoPtion1Name(), allData.getoPtion2Nmae(
            ), allData.getOption3Name(), strTmp[0][z], strTmp[1][z], strTmp[2][z]])
