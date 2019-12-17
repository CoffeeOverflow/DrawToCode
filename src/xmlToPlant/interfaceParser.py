import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataClasses.visibility import Visibility
from src.xmlToPlant.regexExtractors.attributeNameExtractor import AttributeNameExtractor
from src.xmlToPlant.regexExtractors.methodNameExtractor import MethodNameExtractor
from src.xmlToPlant.regexExtractors.parametersExtractor import ParametersExtractor
from src.xmlToPlant.regexExtractors.returnTypeExtractor import ReturnTypeExtractor
from src.xmlToPlant.regexExtractors.visibilityExtractor import VisibilityExtractor


class InterfaceParser:

    @staticmethod
    def read_xml(uml_data: str):
        list_of_methods = []
        list_of_methods_string_literals = []

        html = bs(uml_data, 'html.parser')

        result = html.find_all('p')

        interface_name = result[0].b.string

        list_of_methods_string_literals += str(result[-1]).split("<br>")
        if len(list_of_methods_string_literals) == 1:
            list_of_methods_string_literals = str(result[-1]).split("<br/>")

        list_of_methods_string_literals[0] = \
            list_of_methods_string_literals[0].replace("<p style=\"margin: 0px ; margin-left: 4px\">", "")
        list_of_methods_string_literals[-1] = \
            list_of_methods_string_literals[-1].replace("</p>", "")

        for xml_string in list_of_methods_string_literals:
            if xml_string != "":
                visibility = VisibilityExtractor.extract_visibility(xml_string)

                type_ = ReturnTypeExtractor.extract_type(xml_string)
                name = MethodNameExtractor.extract_name(xml_string)
                list_of_parameters_string = ParametersExtractor.extract_parameters_string(xml_string)

                list_of_parameters = []
                if len(list_of_parameters_string) != 0 and list_of_parameters_string[0] != '':
                    for parameter_string in list_of_parameters_string:
                        parameter_name = AttributeNameExtractor.extract_name(parameter_string)
                        parameter_type = ReturnTypeExtractor.extract_type(parameter_string)
                        parameter = Attribute(parameter_name, parameter_type)
                        list_of_parameters.append(parameter)

                method = Method(name, type_, list_of_parameters, visibility)
                list_of_methods.append(method)

        return Interface(interface_name, list_of_methods)
