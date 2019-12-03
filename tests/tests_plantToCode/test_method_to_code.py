import pytest
from dataToCode.ToJava.methodToJava import MethodToJava
from src.plantToCode.method import Method
from src.plantToCode.visibility import Visibility
from src.plantToCode.attribute import Attribute


def test_method_with_name():
    method = Method("test")
    method_to_code = MethodToJava([method])
    code = method_to_code._MethodToCode__convert_method(method)
    assert code == "public void test()"


visibility_data = [
    ("public", "public void test()"),
    ("private", "private void test()"),
    ("protected", "protected void test()"),
    ("package", "package void test()"),
]


@pytest.mark.parametrize("visibility_name,expected", visibility_data)
def test_method_visibility(visibility_name, expected):
    visibility = Visibility(visibility_name)
    method = Method("test", visibility=visibility)
    method_to_code = MethodToJava([method])
    code = method_to_code._MethodToCode__convert_method(method)
    assert code == expected


value_data = [
    ("int", "public int test()"),
    (None, "public void test()"),
    ("float", "public float test()"),
]


@pytest.mark.parametrize("value,expected", value_data)
def test_method_value(value, expected):
    if not value:
        method = Method("test")
    else:
        method = Method("test", return_type=value)
    method_to_code = MethodToJava([method])
    code = method_to_code._MethodToCode__convert_method(method)
    assert code == expected

parameters_data = [
    ([], "public void test()"),
    ([("a", "int", "public")], "public void test(int a)"),
    ([("b", "int", "public"), ("a", "float", "private")], "public void test(int b, float a)"), 
]


@pytest.mark.parametrize("parameter_list,expected", parameters_data)
def test_method_parameters(parameter_list, expected):
    parameter_list = [Attribute(x, y, z) for x, y, z in parameter_list]
    method = Method("test", parameters=parameter_list)
    method_to_code = MethodToJava([method])
    code = method_to_code._MethodToCode__convert_method(method)
    assert code == expected
