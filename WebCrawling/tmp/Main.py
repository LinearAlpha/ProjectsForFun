#coding: utf-8
import time
import csv
import os
from DataClass import dataClass
from ClickWeb import clickCategory
from ClickWeb import choiseOption
from WebPassing import oneOprionChoicse
from WebPassing import twoOprionChoicse
from WebPassing import threeOprionChoicse

os.chdir("..")
if os.path.isdir("Data"):
    os.chdir("Data")
else:
    os.makedirs("Data")
    os.chdir("Data")

allData = []
categoryName = []

# Coffe
i = 0
clickCategory(i)
categoryName.append()
# This is partial xpath id
option1 = "Manufacturer"
option2 = "Model"
# Collect and store data in to data list
allData.append(twoOprionChoicse(categoryName[i], option1, option2))




    start_time = time.time()
    allData = []
    mainName = []
    for i in range(0, 10):
        # Coffe
        if i == 0:
            setMainMenu(i)
            option1 = "Manufacturer"
            option2 = "Model"
            allData.append(loopingTwo(mainMenuName, option1, option2))
            size = len(allData[0])

        # Espresso
        elif i == 1:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "Espresso"
            allData.append(loopingOne(mainMenuName, option1))
            size = len(allData[1])

        # Fountain
        elif i == 2:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "FountainDrink"
            option2 = "CarbonatorType"
            option3 = "CarbonatorNo"
            allData.append(loopingThree(
                mainMenuName, option1, option2, option3))

        # Frozen Carbonated Beverage
        elif i == 3:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "Manufacturer"
            option2 = "Model"
            allData.append(loopingTwo(mainMenuName, option1, option2))

        # Hot Water Dispensing
        elif i == 4:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "Manufacturer"
            option2 = "Model"
            allData.append(loopingTwo(mainMenuName, option1, option2))

        # Ice
        elif i == 5:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "IceNumber"
            option2 = "IceWeightType"
            option3 = "IceWeightPounds"
            allData.append(loopingThree(
                mainMenuName, option1, option2, option3))

        # Iced Tea
        elif i == 6:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "Manufacturer"
            option2 = "Model"
            allData.append(loopingTwo(mainMenuName, option1, option2))

        # Specialty Beverage
        elif i == 7:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "Manufacturer"
            option2 = "Equipment"
            option3 = "Model"
            allData.append(loopingThree(
                mainMenuName, option1, option2, option3))

        # Steam Oven
        elif i == 8:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "Manufacturer"
            option2 = "Model"
            allData.append(loopingTwo(mainMenuName, option1, option2))

        # Whole Store
        if i == 9:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
            option1 = "Carbonators"
            option2 = "DailyProduction"
            option3 = "brewer"
            allData.append(loopingThree(
                mainMenuName, option1, option2, option3))
        mainName.append(mainMenuName)

    driver.quit()
    print('\n\n\n\n')


    for i in range(0, 10):
        tmpPrint = "i = " + str(i)
        print(tmpPrint)
        strTmp = mainName[i] + ".csv"
        f = open(strTmp, 'w', encoding='utf-8', newline='')
        thewriter = csv.writer(f)
        tmp = strTmp + " is saveing"
        print(tmp)
        max = len(allData[i])
        for j in range(0, max):
            tmpPrint = "j = " + str(j)
            print(tmpPrint)
            data = allData[i]
            dataForSave(thewriter, data[j], allData[i][j].getNumLoop())
        f.close()
        tmp = strTmp + " is saved on" + os.getcwd()
        print(tmp)
