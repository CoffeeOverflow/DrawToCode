import xml.etree.ElementTree as ET
from src.xmlToPlant.classParser import ClassParser
from src.xmlToPlant.interfaceParser import InterfaceParser

class DrawIoXmlParser:

    def __init__(self, filename: str) -> object:
        self.filename = filename

    @staticmethod
    def __extract_value_from_cells(root) -> list:
        list_of_xml_classes = []
        superclass_to_subclasses = {}
        implements_dict = {}

        for cell in root.iter('mxCell'):
            if cell.get('id') not in ['0', '1']:
                if cell.get('value') == 'Extends':
                    subclass = cell.get('source')
                    superclass = cell.get('target')

                    try:
                        superclass_to_subclasses[superclass].append(subclass)
                    except KeyError:
                        superclass_to_subclasses[superclass] = [subclass]

                elif cell.get('value') == "":  # implements arrow
                    source_class = cell.get('source')
                    target_class = cell.get('target')  #interface

                    try:
                        implements_dict[target_class].append(source_class)
                    except KeyError:
                        implements_dict[target_class] = [source_class]
                else:   
                    id = cell.get('id')
                    list_of_xml_classes.append(cell.get('value'))

        print('extends', superclass_to_subclasses)
        print('implements', implements_dict)

        return list_of_xml_classes

    def read_xml(self):
        xml = ET.parse(self.filename)
        root = xml.getroot()

        list_of_xml_classes = self.__extract_value_from_cells(root)

        list_of_classes = []
        list_of_interfaces = []

        for uml_data in list_of_xml_classes:
            if "Interface" in uml_data:
                list_of_interfaces.append(InterfaceParser.read_xml(uml_data))
            else:
                list_of_classes.append(ClassParser.read_xml(uml_data))

        if list_of_classes:
            for class_ in list_of_classes:
                print(class_.name)
                for attribute in class_.fields:
                    print(attribute.visibility, attribute.name, attribute.type_)
                for method in class_.methods:
                    print(method.visibility, method.name, method.return_type)
                    for parameter in method.parameters:
                        print(parameter.name, parameter.type_)

        if list_of_interfaces:
            for interface_ in list_of_interfaces:
                print(interface_.name)
                for method in interface_.methods:
                    print(method.visibility, method.name, method.return_type)
                    for parameter in method.parameters:
                        print(parameter.name, parameter.type_)
