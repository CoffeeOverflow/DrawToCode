import pytest
from src.plantToCode.languages.ToJava.methodToJava import MethodToJava
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataClasses.visibility import Visibility
from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.modifier import Modifier
from typing import List


def test_formatted_method():
    method = Method("example")
    method_to_java = MethodToJava([method], True)
    assert method_to_java.get_formatted_methods() == "\tpublic void example();"

def test_formatted_methods():
    method1 = Method("example")
    method2 = Method("example2")
    method_to_java = MethodToJava([method1, method2], True)
    assert method_to_java.get_formatted_methods() == (f"\tpublic void example();"
                                                     f"\n\n\tpublic void"
                                                     f" example2();")

visibility_data = [
    (Visibility.public, "\tpublic void example();"),
    (Visibility.private, "\tprivate void example();"),
    (Visibility.package, "\tpackage void example();"),
    (Visibility.protected, "\tprotected void example();"), 
]
@pytest.mark.parametrize("visibility, expected", visibility_data)
def test_formatted_method_visibility(visibility, expected):
    method = Method("example", visibility=visibility)
    method_to_java = MethodToJava([method], True)
    assert method_to_java.get_formatted_methods() == expected


type_data = [
    ("int", "\tpublic int example();"),
    ("float", "\tpublic float example();"),
]
@pytest.mark.parametrize("type_name, expected", type_data)
def test_formatted_method_type(type_name, expected):
    method = Method("example", return_type=type_name)
    method_to_java = MethodToJava([method], True)
    assert method_to_java.get_formatted_methods() == expected
    

parameter_data = [
    ([["a", "int"]], "\tpublic void example(int a);"),
    ([["a", "int"], ["b", "float"]], "\tpublic void example(int a, float b);"),
]
@pytest.mark.parametrize("parameters, expected", parameter_data)
def test_formatted_method_parameters(parameters, expected):
    parameter_list: List[Attribute] = []
    for parameter in parameters:
        name, return_type = parameter
        new_parameter = Attribute(name, return_type)
        parameter_list.append(new_parameter)

    method = Method("example", parameters=parameter_list)
    method_to_java = MethodToJava([method], True)
    assert method_to_java.get_formatted_methods() == expected


body_data = [
    (True, "\tpublic void example();"),
    (False, (f"\tpublic void example()"  
             f" {{\n\t\tthrow new UnsupportedOperationException();\n\t}}")),
]
@pytest.mark.parametrize("is_from_interface, expected", body_data)
def test_formatted_method_body(is_from_interface, expected):
    method = Method("example")
    method_to_java = MethodToJava([method], is_from_interface)
    assert method_to_java.get_formatted_methods() == expected


modifier_data = [
    (Modifier.abstract, "\tpublic abstract void example();"),
    (Modifier.override, "\t@override\n\tpublic void example();"),
    (Modifier.static, "\tpublic static void example();"),
]
@pytest.mark.parametrize("modifier, expected", modifier_data)
def test_formatted_method_modifier(modifier, expected):
    method = Method("example", modifier=modifier)
    method_to_java = MethodToJava([method], True)
    print(method_to_java.get_formatted_methods())
    assert method_to_java.get_formatted_methods() == expected
