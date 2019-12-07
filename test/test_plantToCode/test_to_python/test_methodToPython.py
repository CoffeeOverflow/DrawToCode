import pytest
from src.plantToCode.dataToCode.toPython.methodToPython import MethodToPython
from dataClasses.method import Method
from dataClasses.visibility import Visibility
from dataClasses.attribute import Attribute
from dataClasses.modifier import Modifier
from typing import List


def test_formatted_method():
    method = Method("example")
    method_to_python = MethodToPython([method], False)
    assert method_to_python.get_formatted_methods() == (f"\tdef example(self):\n"
                                                        f"\t\tpass")


def test_formatted_methods():
    method1 = Method("example")
    method2 = Method("example2")
    method_to_python = MethodToPython([method1, method2], False)
    expected_one = (f"\tdef example(self):\n"
                    f"\t\tpass")
    expected_two = (f"\tdef example2(self):\n"
                    f"\t\tpass")
    assert method_to_python.get_formatted_methods() == expected_one + "\n\n" + expected_two


visibility_data = [
    (Visibility.public, "\tdef example(self):\n\t\tpass"),
    (Visibility.private, "\tdef __example(self):\n\t\tpass"),
    (Visibility.package, "\tdef example(self):\n\t\tpass"),
    (Visibility.protected, "\tdef _example(self):\n\t\tpass"),
]


@pytest.mark.parametrize("visibility, expected", visibility_data)
def test_formatted_method_visibility(visibility, expected):
    method = Method("example", visibility=visibility)
    method_to_python = MethodToPython([method], False)
    assert method_to_python.get_formatted_methods() == expected


parameter_data = [
    ([["a", "int"]], "\tdef example(self, a):\n\t\tpass"),
    ([["a", "int"], ["b", "float"]], "\tdef example(self, a, b):\n\t\tpass"),
]


@pytest.mark.parametrize("parameters, expected", parameter_data)
def test_formatted_method_parameters(parameters, expected):
    parameter_list: List[Attribute] = []
    for parameter in parameters:
        name, return_type = parameter
        new_parameter = Attribute(name, return_type)
        parameter_list.append(new_parameter)

    method = Method("example", parameters=parameter_list)
    method_to_python = MethodToPython([method], False)
    assert method_to_python.get_formatted_methods() == expected


body_data = [
    (True, "\t@abstractmethod\n\tdef example(self):\n\t\tpass"),
    (False, "\tdef example(self):\n\t\tpass"),
]


@pytest.mark.parametrize("is_from_interface, expected", body_data)
def test_formatted_method_body(is_from_interface, expected):
    method = Method("example")
    method_to_python = MethodToPython([method], is_from_interface)
    assert method_to_python.get_formatted_methods() == expected


modifier_data = [
    (Modifier.abstract, "\t@abstractmethod\n\tdef example(self):\n\t\tpass"),
    (Modifier.override, "\tdef example(self):\n\t\tpass"),
    (Modifier.static, "\t@staticmethod\n\tdef example():\n\t\tpass"),
]


@pytest.mark.parametrize("modifier, expected", modifier_data)
def test_formatted_method_modifier(modifier, expected):
    method = Method("example", modifier=modifier)
    method_to_python = MethodToPython([method], False)
    print(method_to_python.get_formatted_methods())
    assert method_to_python.get_formatted_methods() == expected

def test_static_protected_method_with_parameters():
    param = Attribute("name", "String")
    method = Method("example", "int", [param],
                    Visibility.protected, Modifier.static)
    method_to_python = MethodToPython([method], False)
    expected = "\t@staticmethod\n\tdef _example(name):\n\t\tpass"
    assert method_to_python.get_formatted_methods() == expected

