import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
from src.dataToCode.dataClasses.attribute import Attribute
from src.dataToCode.dataClasses.classData import ClassData
from src.dataToCode.dataClasses.method import Method
from src.dataToCode.dataClasses.visibility import Visibility
from src.xmlToData.regexExtractors.attributeNameExtractor import AttributeNameExtractor
from src.xmlToData.regexExtractors.methodNameExtractor import MethodNameExtractor
from src.xmlToData.regexExtractors.parametersExtractor import ParametersExtractor
from src.xmlToData.regexExtractors.returnTypeExtractor import ReturnTypeExtractor
from src.xmlToData.regexExtractors.visibilityExtractor import VisibilityExtractor


class ClassParser:

    @staticmethod
    def read_xml(uml_data: str):
        uml_data = uml_data.replace("<br>", "")
        uml_data = uml_data.replace("<br/>", "")
        list_of_attributes = []
        list_of_methods = []
        id_to_name = {}

        html = bs(uml_data, 'html.parser')

        result = html.find_all('p')

        class_name = ''

        for i in range(len(result)):
            if result[i].string is not None:
                if i == 0:
                    class_name = result[i].b.string
                    id_to_name[id] = class_name
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
                                parameter = Attribute(parameter_name, parameter_type)
                                list_of_parameters.append(parameter)

                        method = Method(name, type_, list_of_parameters, visibility)
                        list_of_methods.append(method)
                    else:
                        name = AttributeNameExtractor.extract_name(result[i].string)
                        attribute = Attribute(name, type_, visibility)
                        list_of_attributes.append(attribute)

        return ClassData(class_name, list_of_attributes, list_of_methods)
