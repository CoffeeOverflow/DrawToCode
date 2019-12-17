from src.dataToCode.dataClasses.attribute import Attribute
import pytest
from src.dataToCode.dataClasses.visibility import Visibility
from src.dataToCode.dataClasses.method import Method

def test_method_equal():
    a = Method("a")
    b = Method("a")
    output = (a == b)
    assert output == True

def test_method_not_equal_name():
    a = Method("a")
    b = Method("b")
    output = (a == b)
    assert output == False

def test_method_diffent_param_number():
    a = Method("a")
    parameter = Attribute("a", "int")
    b = Method("a", parameters=[parameter])
    output = (a == b)
    assert output == False

def test_method_equal_param():
    parameter1 = Attribute("a", "int")
    parameter2 = Attribute("a", "int")
    a = Method("a", parameters=[parameter1])
    b = Method("a", parameters=[parameter2])
    output = (a == b)
    assert output == True

def test_method_not_equal_param():
    parameter1 = Attribute("b", "int")
    parameter2 = Attribute("a", "int")
    a = Method("a", parameters=[parameter1])
    b = Method("a", parameters=[parameter2])
    output = (a == b)
    assert output == False

def test_method_equal_params():
    parameter1 = Attribute("a", "int")
    parameter2 = Attribute("a", "int")
    parameter3 = Attribute("b", "int")
    parameter4 = Attribute("b", "int")
    a = Method("a", parameters=[parameter1, parameter3])
    b = Method("a", parameters=[parameter2, parameter4])
    output = (a == b)
    assert output == True

def test_method_not_equal_params():
    parameter1 = Attribute("a", "int")
    parameter2 = Attribute("a", "int")
    parameter3 = Attribute("b", "int")
    parameter4 = Attribute("c", "int")
    a = Method("a", parameters=[parameter1, parameter3])
    b = Method("a", parameters=[parameter2, parameter4])
    output = (a == b)
    assert output == False

def test_method_params_unordered():
    parameter1 = Attribute("a", "int")
    parameter2 = Attribute("a", "int")
    parameter3 = Attribute("b", "int")
    parameter4 = Attribute("b", "int")
    a = Method("a", parameters=[parameter1, parameter3])
    b = Method("a", parameters=[parameter4, parameter2])
    output = (a == b)
    assert output == False
