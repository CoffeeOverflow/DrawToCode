import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataClasses.visibility import Visibility
from src.xmlToPlant.classParser import ClassParser
from src.xmlToPlant.regexExtractors.attributeNameExtractor import AttributeNameExtractor
from src.xmlToPlant.regexExtractors.methodNameExtractor import MethodNameExtractor
from src.xmlToPlant.regexExtractors.parametersExtractor import ParametersExtractor
from src.xmlToPlant.regexExtractors.returnTypeExtractor import ReturnTypeExtractor
from src.xmlToPlant.regexExtractors.visibilityExtractor import VisibilityExtractor


class DrawIoXmlParser:

    def __init__(self, filename: str) -> object:
        self.filename = filename

    @staticmethod
    def __extract_value_from_cells(root) -> list:
        list_of_xml_classes = []

        for cell in root.iter('mxCell'):
            if cell.get('id') not in ['0', '1']:
                if cell.get('value') == 'Extends':
                    arrow_type = 'Extends'
                    source_class = cell.get('source') #subclasse
                    target_class = cell.get('target') #superclasse
                elif cell.get('value') is not None: #implements arrow
                    arrow_type = 'Implements'
                    source_class = cell.get('source')
                    target_class = cell.get('target')  #interface
                else:   
                    id = cell.get('id')
                    list_of_xml_classes.append(cell.get('value'))

        return list_of_xml_classes

    def read_xml(self):
        xml = ET.parse(self.filename)
        root = xml.getroot()

        list_of_xml_classes = self.__extract_value_from_cells(root)

        list_of_classes = []

        for uml_data in list_of_xml_classes:
            if "Interface" in uml_data:
                print("Error")
            else:
                list_of_classes.append(ClassParser.read_xml(uml_data))

        for class_ in list_of_classes:
            print(class_.name)
            for attribute in class_.fields:
                print(attribute.visibility, attribute.name, attribute.type_)
            for method in class_.methods:
                print(method.visibility, method.name, method.return_type)
                for parameter in method.parameters:
                    print(parameter.name, parameter.type_)
