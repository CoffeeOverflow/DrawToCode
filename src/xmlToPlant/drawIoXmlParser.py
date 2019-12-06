import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from src.plantToCode.attribute import Attribute
from src.plantToCode.classData import ClassData
from src.plantToCode.method import Method
from src.plantToCode.visibility import Visibility
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
                if cell.get('value') in ['Extends', 'Use']:
                    arrow_type = cell.get('value')
                    source_class = cell.get('source')
                    target_class = cell.get('target')
                else:
                    list_of_xml_classes.append(cell.get('value'))

        return list_of_xml_classes

    def read_xml(self):
        xml = ET.parse(self.filename)
        root = xml.getroot()

        list_of_xml_classes = self.__extract_value_from_cells(root)

        list_of_classes = []

        for uml_data in list_of_xml_classes:

            list_of_attributes = []
            list_of_methods = []

            print(uml_data)

            html = bs(uml_data, 'html.parser')

            result = html.find_all('p')

            class_name = ''

            for i in range(len(result)):
                if result[i].string is not None:
                    if i == 0:
                        class_name = result[i].string
                    else:
                        visibility = VisibilityExtractor.extract_visibility(result[i].string)
                        type_ = ReturnTypeExtractor.extract_type(result[i].string)

                        if '(' in result[i].string:
                            name = MethodNameExtractor.extract_name(result[i].string)

                            list_of_parameters_string = ParametersExtractor.extract_parameters_string(result[i].string)

                            list_of_parameters = []
                            if len(list_of_parameters_string) != 0 and list_of_parameters_string[0] != '':
                                for parameter_string in list_of_parameters_string:
                                    parameter_name = AttributeNameExtractor.extract_name(parameter_string)
                                    parameter_type = ReturnTypeExtractor.extract_type(parameter_string)
                                    parameter = Attribute(parameter_name, parameter_type, Visibility.public)
                                    list_of_parameters.append(parameter)

                            method = Method(name, type_, list_of_parameters, visibility)
                            list_of_methods.append(method)
                        else:
                            name = AttributeNameExtractor.extract_name(result[i].string)
                            attribute = Attribute(name, type_, visibility)
                            list_of_attributes.append(attribute)

            list_of_classes.append(ClassData(class_name, list_of_attributes, list_of_methods))
        for class_ in list_of_classes:
            print(class_.name)
            for attribute in class_.fields:
                print(attribute.visibility, attribute.name, attribute.type_)
            for method in class_.methods:
                print(method.visibility, method.name, method.return_type)
                for parameter in method.parameters:
                    print(parameter.name, parameter.type_)
