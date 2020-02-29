#coding: utf-8
import time
from guiSetting import setMainMenu
from guiGet import getNameMainMenu
from proseccForPassing import loopingOne
from proseccForPassing import loopingTwo
from proseccForPassing import loopingThree

start_time = time.time()
for i in range(0, 10):

    # Coffe
    if i == 0:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "Manufacturer"
        option2 = "Model"
        loopingTwo(option1, option2)

    # Espresso
    elif i == 1:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "Espresso"
        loopingOne(option1)
    
    # Fountain
    elif i == 2:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "FountainDrink"
        option2 = "CarbonatorType"
        option3 = "CarbonatorNo"
        loopingThree(option1, option2, option3)

    # Frozen Carbonated Beverage
    elif i == 3:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "Manufacturer"
        option2 = "Model"
        loopingTwo(option1, option2)

    # Hot Water Dispensing
    elif i == 4:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "Manufacturer"
        option2 = "Model"
        loopingTwo(option1, option2)

    # Ice 
    elif i == 5:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "IceNumber"
        option2 = "IceWeightType"
        option3 = "IceWeightPounds"
        loopingThree(option1, option2, option3)

    # Iced Tea
    elif i == 6:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "Manufacturer"
        option2 = "Model"
        loopingTwo(option1, option2)

    # Specialty Beverage
    elif i == 7:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "Manufacturer"
        option2 = "Equipment"
        option3 = "Model"
        loopingThree(option1, option2, option3)

    # Steam Oven
    elif i == 8:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "Manufacturer"
        option2 = "Model"
        loopingTwo(option1, option2)

    # Whole Store
    elif i == 9:
        setMainMenu(i)
        tmp = "i = " + str(i)
        tmp = tmp + "\t" + getNameMainMenu(i)
        option1 = "Carbonators"
        option2 = "DailyProduction"
        option3 = "brewer"
        loopingThree(option1, option2, option3)

print("--- %s seconds ---" % (time.time() - start_time))
