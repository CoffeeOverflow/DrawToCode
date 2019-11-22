import pytest
from src.plantToCode.classData import ClassData
from src.plantToCode.inheritanceToCode import InheritanceToCode


def test_no_inheritance():
    assert InheritanceToCode([]).get_formatted() == ""


def test_with_one_inheritance():
    class1 = ClassData("class1")

    inheritance_to_code = InheritanceToCode([class1])
    expected = " extends class1"

    assert inheritance_to_code.get_formatted() == expected


def test_with_two_inheritances():
    class1 = ClassData("class1")
    class2 = ClassData("class2")

    inheritance_to_code = InheritanceToCode([class1, class2])
    expected = " extends class1, class2"

    assert inheritance_to_code.get_formatted() == expected


def test_with_five_inheritances():
    classes = [ClassData("c1"),
               ClassData("c2"),
               ClassData("c3"),
               ClassData("c4"),
               ClassData("c5")]

    inheritance_to_code = InheritanceToCode(classes)
    expected = " extends c1, c2, c3, c4, c5"

    assert inheritance_to_code.get_formatted() == expected
