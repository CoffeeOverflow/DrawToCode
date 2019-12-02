import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from src.xmlToPlant.regex.XMLCodeExtractor import  XMLCodeExtractor

class readXml:

    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        xml = ET.parse(self.filename)
        root = xml.getroot()

        for cell in root.iter('mxCell'):
            if(int(cell.get('id')) > 1):
                #print(cell.get('id'))
                uml_data = cell.get('value')
                #print(uml_data)

        html = bs(uml_data, 'html.parser')
        #print(html.prettify())

        result = html.find_all('p')

        for i in range(len(result) - 1):
            if i == 0:
                print(result[i].b.string)
            else:
                print(XMLCodeExtractor.extract_visibility(result[i].string),
                      XMLCodeExtractor.extract_name(result[i].string),
                      XMLCodeExtractor.extract_type(result[i].string))