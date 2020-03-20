'''
File: WebDataClass.py
Author: Minpto Kim
Projrct: WebCrawling
Description:
    Class for the data sourced from the everpuresizing
'''
#coding: utf-8

class webData:
    category = ""
    option1Name = ""
    option2Nmae = ""
    option3Name = ""
    productInfo = []
    numOption = 0
    prodctSystem = False

    def __init__(self):
        pass

    def setCategory(self, category):
        self.category = category

    def setOptionOne(self, option1):
        self.option1Name = option1

    def setOptionTwo(self, option2):
        self.option2Nmae = option2

    def setOptionThree(self, option3):
        self.option3Name = option3

    def setProductInfo(self, productInfo):
        self.productInfo = productInfo

    def setNumOption(self, numOption):
        self.numOption = numOption

    def setProductSystem(self, prodctSystem):
        self.prodctSystem = prodctSystem

    def getCategory(self):
        return self.category

    def getOptionOne(self):
        return self.option1Name

    def getOptionTwo(self):
        return self.option2Nmae

    def getOptionThree(self):
        return self.option3Name

    def getNumOption(self):
        return self.numOption

    def getProducSystem(self):
        return self.prodctSystem
