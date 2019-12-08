import pytest

from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataClasses.visibility import Visibility
from src.xmlToPlant.drawIoXmlParser import DrawIoXmlParser
import os.path as path


def test_interfaces_returned_read_xml():
    examples_folder = path.abspath(path.join(__file__, "../../../src/xmlToPlant/uml_samples/uml_interface.xml"))
    interface_ = Interface("CalculoDeSalario", [Method("calcular_salario_1", "float",
        [Attribute("funcionario", "Funcionario")]), Method("calcular_salario_2", "float",
        [Attribute("funcionario", "Funcionario"), Attribute("carga_horaria", "int")])], Visibility.public)
    list_of_classes, list_of_interfaces = DrawIoXmlParser(examples_folder).read_xml()
    assert list_of_interfaces[0].name == interface_.name
    assert list_of_interfaces[0].visibility == interface_.visibility
    for method_actual, method_expected in zip(list_of_interfaces[0].methods, interface_.methods):
        assert method_actual.name == method_expected.name
        assert method_actual.visibility == method_expected.visibility
        assert method_actual.return_type == method_expected.return_type
        for parameter_actual, parameter_expected in zip(method_actual.parameters, method_expected.parameters):
            assert parameter_actual.name == parameter_expected.name
            assert parameter_actual.visibility == parameter_expected.visibility
            assert parameter_actual.type_ == parameter_expected.type_

def test_classes_returned_read_xml():
    examples_folder = path.abspath(path.join(__file__, "../../../src/xmlToPlant/uml_samples/uml1.xml"))
    class_ = ClassData("Humano", [Attribute("idade", "int", Visibility.public), Attribute("anos", "float", Visibility.private)],
                       [Method("get_idade", "int", [Attribute("nome", "string"), Attribute("altura", "double")],
                        Visibility.public), Method("get_anos", "float", [], Visibility.private)])
    list_of_classes, list_of_interfaces = DrawIoXmlParser(examples_folder).read_xml()
    assert list_of_classes[0].name == class_.name
    assert list_of_classes[0].visibility == class_.visibility
    for method_actual, method_expected in zip(list_of_classes[0].methods, class_.methods):
        assert method_actual.name == method_expected.name
        assert method_actual.visibility == method_expected.visibility
        assert method_actual.return_type == method_expected.return_type
        for parameter_actual, parameter_expected in zip(method_actual.parameters, method_expected.parameters):
            assert parameter_actual.name == parameter_expected.name
            assert parameter_actual.visibility == parameter_expected.visibility
            assert parameter_actual.type_ == parameter_expected.type_
        for attribute_actual, attribute_expected in zip(list_of_classes[0].fields, class_.fields):
            assert attribute_actual.name == attribute_expected.name
            assert attribute_actual.visibility == attribute_expected.visibility
            assert attribute_actual.type_ == attribute_expected.type_
