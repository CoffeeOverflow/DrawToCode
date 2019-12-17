import pytest

from src.dataToCode.dataClasses.attribute import Attribute
from src.dataToCode.dataClasses.classData import ClassData
from src.dataToCode.dataClasses.interface import Interface
from src.dataToCode.dataClasses.method import Method
from src.dataToCode.dataClasses.visibility import Visibility
from src.xmlToData.drawIoXmlParser import DrawIoXmlParser
import os.path as path
import xml.etree.ElementTree as ET


def test_interfaces_returned_read_xml():
    examples_folder = path.abspath(path.join(__file__, "../../../src/xmlToData/uml_samples/uml_interface.xml"))
    interface_ = Interface("CalculoDeSalario", [Method("calcular_salario_1", "float",
                                                       [Attribute("funcionario", "Funcionario")]),
                                                Method("calcular_salario_2", "float",
                                                       [Attribute("funcionario", "Funcionario"),
                                                        Attribute("carga_horaria", "int")])], Visibility.public)
    list_of_classes, list_of_interfaces = DrawIoXmlParser(examples_folder).read_xml()
    assert list_of_interfaces[0] == interface_


def test_classes_returned_read_xml():
    examples_folder = path.abspath(path.join(__file__, "../../../src/xmlToData/uml_samples/uml1.xml"))
    class_ = ClassData("Humano",
                       [Attribute("idade", "int", Visibility.public), Attribute("anos", "float", Visibility.private)],
                       [Method("get_idade", "int", [Attribute("nome", "string"), Attribute("altura", "double")],
                               Visibility.public), Method("get_anos", "float", [], Visibility.private)])
    list_of_classes, list_of_interfaces = DrawIoXmlParser(examples_folder).read_xml()
    assert list_of_classes[0] == class_


def test_extract_value_from_cells():
    examples_folder = path.abspath(path.join(__file__, "../../../src/xmlToData/uml_samples/uml_interface.xml"))
    xml = ET.parse(examples_folder)
    root = xml.getroot()
    list_of_ids = ['-cuIEp4vuOl5B3aBU6dm-1']
    list_of_xml_classes = [
        "<p style=\"margin: 0px ; margin-top: 4px ; text-align: center\"><i>&lt;&lt;Interface&gt;&gt;</i><br><b>CalculoDeSalario</b></p><hr size=\"1\"><p style=\"margin: 0px ; margin-left: 4px\">+ calcular_salario_1(funcionario: Funcionario): float<br>+ calcular_salario_2(funcionario: Funcionario, carga_horaria: int): float</p>"]
    list_of_xml_classes_, list_of_ids_, superclass_to_subclasses, implements_dict = \
        DrawIoXmlParser.extract_value_from_cells(root)
    assert implements_dict == {}
    assert superclass_to_subclasses == {}
    assert list_of_xml_classes == list_of_xml_classes_
    assert list_of_ids == list_of_ids_


def test():
    examples_folder = path.abspath(path.join(__file__, "../../../src/xmlToData/uml_samples/orcs.xml"))
    a = DrawIoXmlParser(examples_folder)
    class_list, interface_list = a.read_xml()

    for class_ in class_list:
        print(class_.name)
        for attribute in class_.fields:
            print(attribute.visibility, attribute.name, attribute.type_)
        for method in class_.methods:
            print(method.visibility, method.name, method.return_type)
            for parameter in method.parameters:
                print(parameter.name, parameter.type_)
        print()

    for interface_ in interface_list:
        print(interface_.name)
        for method in interface_.methods:
            print(method.visibility, method.name, method.return_type)
            for parameter in method.parameters:
                print(parameter.name, parameter.type_)
        print()
