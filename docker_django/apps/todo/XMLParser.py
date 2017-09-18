import xml.etree.ElementTree as ET


class HemslXMLParser:
    def __init__(self, xmlFilePath):
        self.xmlFilePath = xmlFilePath

    """ utf-8的中文编码是3个字节，第一个字节的前4位，第二第三字节的前两位掐掉，剩余部分拼接起来，就是汉字实际的unicode值 """
    def stringFotmat(slef, str):
        value_bytes = b''
        length = len(str)

        result_str = ''

        for i in range(0, length, 1):
            temp_bytes = bytes(str[i], encoding='utf-8')
            if len(temp_bytes) == 3:
                print(str[i])
                str_a = temp_bytes[0]
                str_b = temp_bytes[1]
                str_c = temp_bytes[2]
                value_a = (str_a & 0b00001111) << 4
                value_b1 = (str_b & 0b00111111) >> 2
                value_b2 = (str_b & 0b00000011) << 6
                value_c = str_c & 0b00111111
                #print(value_a + value_b1)
                first_value = hex(value_a + value_b1)
                second_value = hex(value_b2 + value_c)
                if len(first_value) < 4: #有的汉字是用个位数的16进制可以表达的，需要补0
                    first_value = '0x0' + first_value[2:]
                if len(second_value) < 4: #有的汉字是用个位数的16进制可以表达的，需要补0
                    second_value = '0x0' + second_value[2:]
                #print(type(first_value))
                #print(first_value)
                #print(second_value)
                result_bytes = b''
                #print(type(result_bytes))
                result_bytes += b'\u' + bytes(first_value, encoding='utf-8')[2:] + bytes(second_value, encoding='utf-8')[2:]
                #print(type(result_bytes))
                #print(result_bytes.decode('unicode_escape'))
                value_bytes += result_bytes
                #print(result_bytes.decode('unicode_escape'))
                #hex(str_a)[len():]
            else:
                value_bytes += bytes(str[i], encoding='utf-8')
                #print(i)
        return value_bytes.decode('unicode_escape')


    def getAttribVlue(self, attribName):
        tree = ET.parse(self.xmlFilePath)
        root = tree.getroot()
        value = ''
        #print(root)
        for string in root.findall('string'):
            #print(string)
            name = string.get('name')
            if name == attribName:
                print(string.text)
            #if value != None:
                return self.stringFotmat(string.text)
        return value
