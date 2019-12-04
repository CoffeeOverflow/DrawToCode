import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs

'''from src.plantToCode.classData import ClassData
from src.plantToCode.attribute import Attribute
from src.plantToCode.method import Method'''
from src.xmlToPlant.regex.xmlCodeExtractor import XMLCodeExtractor


class DrawIoXmlParser:

    def __init__(self, filename: str) -> object:
        self.filename = filename

    def __extract_value_from_cells(self, root) -> list:
        list_of_xml_classes = []
        for cell in root.iter('mxCell'):
            if cell.get('id') != '1' and cell.get('id') != '0':
                list_of_xml_classes.append(cell.get('value'))

        return list_of_xml_classes

    def read_xml(self):
        xml = ET.parse(self.filename)
        root = xml.getroot()

        list_of_xml_classes = self.__extract_value_from_cells(root)

        for uml_data in list_of_xml_classes:

            html = bs(uml_data, 'html.parser')

            result = html.find_all('p')

            '''list_of_classes = [ClassData]
            list_of_attributes = [Attribute]
            list_of_methods = [Method]
            list_of_parameters = [Attribute]'''

            """dict_of_classes = {'classes': {'attributes': {'visibility': str, 'type': str, 'name': str},
                                           'methods': {'visibility': str, 'type': str, 'name': str, 'parameters': list},
                                           'name': str, 'type': str, 'visibility': str}}"""

            for i in range(len(result)):
                if result[i].string is not None:
                    if i == 0:
                        print()
                        print('Class Name:', result[i].string)
                    else:
                        v = XMLCodeExtractor.extract_visibility(result[i].string)
                        n = XMLCodeExtractor.extract_name(result[i].string)
                        t = XMLCodeExtractor.extract_type(result[i].string)
                        p = XMLCodeExtractor.extract_parameters_string(result[i].string)

                        print('Visibility:', v,
                              'Name:', n,
                              'Type:', t)

                        if len(p) != 0 and p[0] != '':
                            for parameter_string in p:
                                print('Parameter Name:', XMLCodeExtractor.extract_name(parameter_string),
                                      'Parameter Type:', XMLCodeExtractor.extract_type(parameter_string))