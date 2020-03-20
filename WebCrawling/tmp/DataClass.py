
class dataClass:
    mainName = ""
    option1Name = ""
    option2Nmae = ""
    option3Name = ""
    productInfo = ["", "", ""]
    numLoop = 0
    system = False

    def __init__(self):
        pass

    def setMainName(self, mainName):
        self.mainName = mainName

    def setOption1Name(self, option1Name):
        self.option1Name = option1Name

    def setOption2Name(self, option2Nmae):
        self.option2Nmae = option2Nmae

    def setOption3Name(self, option3Name):
        self.option3Name = option3Name

    def setProductInfo(self, productInfo):
        self.productInfo = productInfo

    def setNumLoop(self, numLoop):
        self.numLoop = numLoop
    
    def setSystem(self, system):
        self.system = system

    def getMainName(self):
        return self.mainName

    def getoPtion1Name(self):
        return self.option1Name

    def getoPtion2Nmae(self):
        return self.option2Nmae

    def getOption3Name(self):
        return self.option3Name

    def getProductInfo(self):
        return self.productInfo

    def getNumLoop(self):
        return self.numLoop

    def getSystem(self, system):
        return self.system