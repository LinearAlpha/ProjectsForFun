from TrigalClick import clickOption
from DataCapturing import numElement
from WebScraping import numOptionTwo

def byManifactura(category):
    clickOption("IceOneHow", 1)
    option1 = "Manufacturer"
    option2 = "Model"
    return numOptionTwo(category, option1, option2)

def byWeight(category):
    clickOption("IceOneHow", 2)
    option1 = "IceWeightType"
    option2 = "IceWeightPounds"
    tmp = []
    tmp.append(numOptionTwo(category, option1, option2))
    clickOption("IceNumber", 1)
    option1 = "IceWeightType"
    option2 = "IceWeightPounds"
    tmp.append(numOptionTwo(category, option1, option2))
    return tmp