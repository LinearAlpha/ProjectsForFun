#coding: utf-8
import time
import multiprocessing
import threading
from guiSetting import setMainMenu
from guiGet import getNameMainMenu
from proseccForPassing import loopingOne
from proseccForPassing import loopingTwo
from proseccForPassing import loopingThree
import dataClass
from connect import driver
from dataPreOut import dataForSave
import csv
import os

if __name__ == '__main__':
    start_time = time.time()
    allData = []
    mainName = []
    for i in range(0, 10):
        # Coffe
        if i == 0:
            setMainMenu(i)
            mainMenuName = getNameMainMenu(i)
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
    
    os.chdir("..")
    if os.path.isdir("Data"):
        os.chdir("Data")
    else:
        os.makedirs("Data")
        os.chdir("Data")

    for i in range(0, 10):
        strTmp = mainName[i] + ".csv"
        f = open(strTmp, 'w', encoding='utf-8', newline='')
        thewriter = csv.writer(f)
        tmp = strTmp + " is saveing"
        print(tmp)
        max = len(allData[i])
        for j in range(0, max):
            data = allData[i]
            dataForSave(thewriter, data[j], allData[i][j].getNumLoop())
        f.close()
        tmp = strTmp + " is saved on" + os.getcwd()
        print(tmp)
        
    print("--- %s seconds ---" % (time.time() - start_time))
    print("everpuresizing.com web crawling is Finished")
