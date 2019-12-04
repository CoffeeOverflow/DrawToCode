import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs

from src.plantToCode.attribute import Attribute
from src.plantToCode.visibility import Visibility
from src.xmlToPlant.regexExtractors.attributeNameExtractor import AttributeNameExtractor
from src.xmlToPlant.regexExtractors.methodNameExtractor import MethodNameExtractor
from src.xmlToPlant.regexExtractors.parametersExtractor import ParametersExtractor
from src.xmlToPlant.regexExtractors.returnTypeExtractor import ReturnTypeExtractor
from src.xmlToPlant.regexExtractors.visibilityExtractor import VisibilityExtractor

'''from src.plantToCode.classData import ClassData
from src.plantToCode.attribute import Attribute
from src.plantToCode.method import Method'''


class DrawIoXmlParser:

    def __init__(self, filename: str) -> object:
        self.filename = filename

    @staticmethod
    def __extract_value_from_cells(root) -> list:
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

            for i in range(len(result)):
                if result[i].string is not None:
                    if i == 0:
                        print()
                        # print('Class Name:', result[i].string)
                        classname = result[i].string
                        print(classname)
                    else:

                        visibility = VisibilityExtractor.extract_visibility(result[i].string)
                        type_ = ReturnTypeExtractor.extract_type(result[i].string)

                        if '(' in result[i].string:
                            name = MethodNameExtractor.extract_name(result[i].string)

                            list_of_parameters_string = ParametersExtractor.extract_parameters_string(result[i].string)

                            list_of_parameters = []
                            if len(list_of_parameters_string) != 0 and list_of_parameters_string[0] != '':
                                list_of_parameters = []
                                for parameter_string in list_of_parameters_string:
                                    parameter_name = AttributeNameExtractor.extract_name(parameter_string)
                                    parameter_type = ReturnTypeExtractor.extract_type(parameter_string)
                                    attribute = Attribute(parameter_name, parameter_type, Visibility.public)
                                    list_of_parameters.append(attribute)
                        else:
                            name = AttributeNameExtractor.extract_name(result[i].string)
                            list_of_parameters = []

                        print("Visibility:", visibility, "Name:", name, "Return Type:", type_)
                        if len(list_of_parameters) > 0:
                            for parameter in list_of_parameters:
                                print("Parameter name:", parameter.name, "Parameter type:", parameter.type_)
