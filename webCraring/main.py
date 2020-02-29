#coding: utf-8
from guiSetting import setMainMenu
from guiSetting import setManufacturer
from guiSetting import setModel
from guiGet import getNameMainMenu
from guiGet import getNameManufacturer
from guiGet import getNameModel

for i in range(0, 10):
    if i == 0:
        setMainMenu(i)
        for j in range(0, 200):
            setManufacturer(62)
            #for k in range(0, 10000):
               # setModel(51)
    #strTmp = getNameManufacturer(62)
    #print(strTmp)
