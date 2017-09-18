import xml.etree.ElementTree as ET


class HemslXMLParser:
    def __init__(self, xmlFilePath):
        self.xmlFilePath = xmlFilePath

    def getAttribVlue(self, attribName):
        tree = ET.parse(self.xmlFilePath)
        root = tree.getroot()
        value = ''
        #print(root)
        for string in root.findall('string'):
            #print(string)
            name = string.get('name')
            if name == attribName:
                #print(string.text)
            #if value != None:
                return string.text
        return value
