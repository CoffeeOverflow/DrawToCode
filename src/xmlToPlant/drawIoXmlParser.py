import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from src.xmlToPlant.regex.XMLCodeExtractor import XMLCodeExtractor


class DrawIoXmlParser:

    def __init__(self, filename: str) -> object:
        self.filename = filename

    def readXml(self):
        xml = ET.parse(self.filename)
        root = xml.getroot()

        html = self.__extract_value_from_cells(root)

        result = html.find_all('p')

        for i in range(len(result) - 1):
            if i == 0:
                print(result[i].b.string)
            else:
                print(XMLCodeExtractor.extract_visibility(result[i].string),
                      XMLCodeExtractor.extract_name(result[i].string),
                      XMLCodeExtractor.extract_type(result[i].string),
                      XMLCodeExtractor.extract_parameters(result[i].string))

    def __extract_value_from_cells(self, root) -> bs:
        for cell in root.iter('mxCell'):
            if (int(cell.get('id')) > 1):
                uml_data = cell.get('value')
        html = bs(uml_data, 'html.parser')
        return html
