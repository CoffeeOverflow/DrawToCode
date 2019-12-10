from src.plantToCode.dataClasses.attribute import Attribute
import pytest
from src.plantToCode.dataClasses.visibility import Visibility
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataClasses.interface import Interface

def test_interface_equal():
    method1 = Method("a")
    method2 = Method("a")
    a = Interface("a", methods=[method1])
    b = Interface("a", methods=[method2])
    output = a==b
    assert output == True


def test_interface_not_equal_name():
    method1 = Method("a")
    method2 = Method("a")
    a = Interface("a", methods=[method1])
    b = Interface("b", methods=[method2])
    output = a==b
    assert output == False


def test_interface_diffent_method_number():
    method1 = Method("a")
    method2 = Method("a")
    method3 = Method("b")
    a = Interface("a", methods=[method1])
    b = Interface("a", methods=[method2, method3])
    output = a==b
    assert output == False


def test_interface_equal_method():
    method1 = Method("a")
    method2 = Method("a")
    method3 = Method("b")
    method4 = Method("b")
    a = Interface("a", methods=[method1, method4])
    b = Interface("a", methods=[method2, method3])
    output = a==b
    assert output == True


def test_interface_not_equal_method():
    method1 = Method("a")
    method2 = Method("a")
    method3 = Method("b")
    method4 = Method("c")
    a = Interface("a", methods=[method1, method4])
    b = Interface("a", methods=[method2, method3])
    output = a==b
    assert output == False


def test_interface_methods_unordered():
    method1 = Method("a")
    method2 = Method("a")
    method3 = Method("b")
    method4 = Method("b")
    a = Interface("a", methods=[method1, method4])
    b = Interface("a", methods=[method3, method2])
    output = a==b
    assert output == False
