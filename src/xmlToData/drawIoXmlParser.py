import xml.etree.ElementTree as ET
from typing import Tuple, Dict

from src.xmlToData.classParser import ClassParser
from src.xmlToData.interfaceParser import InterfaceParser


class DrawIoXmlParser:

    def __init__(self, filename: str) -> object:
        self.filename = filename

    @staticmethod
    def extract_value_from_cells(root) -> Tuple[list, list, Dict[str, list], Dict[str, list]]:
        list_of_xml_classes = []
        list_of_ids = []
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

                elif "endArrow=block;dashed=1" in cell.get('style'):  # implements arrow
                    source_class = cell.get('source')
                    target_class = cell.get('target')  # interface

                    try:
                        implements_dict[target_class].append(source_class)
                    except KeyError:
                        implements_dict[target_class] = [source_class]
                elif "endArrow" not in cell.get('style'):
                    list_of_ids.append(cell.get('id'))
                    list_of_xml_classes.append(cell.get('value'))

        return list_of_xml_classes, list_of_ids, superclass_to_subclasses, implements_dict

    def read_xml(self):
        xml = ET.parse(self.filename)
        root = xml.getroot()

        list_of_xml_classes, ids_list, extends_dict, implements_dict = self.extract_value_from_cells(root)

        list_of_classes = []
        list_of_interfaces = []
        ids_to_names = {}

        for uml_data, class_id in zip(list_of_xml_classes, ids_list):
            if "Interface" in uml_data:
                interface_ = InterfaceParser.read_xml(uml_data)
                list_of_interfaces.append(interface_)
                ids_to_names[class_id] = interface_.name
            else:
                class_ = ClassParser.read_xml(uml_data)
                list_of_classes.append(class_)
                ids_to_names[class_id] = class_.name

        for superclass_id, subclasses in extends_dict.items():
            superclass_name = ids_to_names[superclass_id]
            for subclass_id in subclasses:
                subclass_name = ids_to_names[subclass_id]
                for class_ in list_of_classes:
                    if class_.name == subclass_name:
                        list_of_inheritances = class_.inheritances.copy()
                        for superclass_ in list_of_classes:
                            if superclass_name == superclass_.name:
                                list_of_inheritances.append(superclass_)
                        class_.inheritances = list_of_inheritances.copy()

        for interface_id, subclasses in implements_dict.items():
            interface_name = ids_to_names[interface_id]
            for class_id in subclasses:
                class_name = ids_to_names[class_id]
                for class_ in list_of_classes:
                    if class_.name == class_name:
                        list_of_interfaces_implemented = class_.implementations.copy()
                        for interface_ in list_of_interfaces:
                            if interface_name == interface_.name:
                                list_of_interfaces_implemented.append(interface_)
                        class_.implementations = list_of_interfaces_implemented.copy()

        return list_of_classes, list_of_interfaces
