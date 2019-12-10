from src.plantToCode.dataClasses.attribute import Attribute
import pytest
from src.plantToCode.dataClasses.visibility import Visibility
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataClasses.classData import ClassData

def test_class_equal():
    method1 = Method("a")
    method2 = Method("a")
    a = ClassData("a", methods=[method1])
    b = ClassData("a", methods=[method2])
    output = a==b
    assert output == True


def test_class_data_not_equal_name():
    method1 = Method("a")
    method2 = Method("a")
    a = ClassData("a", methods=[method1])
    b = ClassData("b", methods=[method2])
    output = a==b
    assert output == False


def test_class_data_diffent_method_number():
    method1 = Method("a")
    method2 = Method("a")
    method3 = Method("b")
    a = ClassData("a", methods=[method1])
    b = ClassData("a", methods=[method2, method3])
    output = a==b
    assert output == False


def test_class_data_equal_method():
    method1 = Method("a")
    method2 = Method("a")
    method3 = Method("b")
    method4 = Method("b")
    a = ClassData("a", methods=[method1, method4])
    b = ClassData("a", methods=[method2, method3])
    output = a==b
    assert output == True


def test_class_data_not_equal_method():
    method1 = Method("a")
    method2 = Method("a")
    method3 = Method("b")
    method4 = Method("c")
    a = ClassData("a", methods=[method1, method4])
    b = ClassData("a", methods=[method2, method3])
    output = a==b
    assert output == False


def test_class_data_methods_unordered():
    method1 = Method("a")
    method2 = Method("a")
    method3 = Method("b")
    method4 = Method("b")
    a = ClassData("a", methods=[method1, method4])
    b = ClassData("a", methods=[method3, method2])
    output = a==b
    assert output == False
