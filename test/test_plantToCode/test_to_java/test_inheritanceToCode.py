import pytest
from src.plantToCode.dataToCode.ToJava.inheritanceToJava import InheritanceToJava
from dataClasses.classData import ClassData


def test_no_inheritance_equals_empty_string():
    assert InheritanceToJava([]).get_formatted() == ''


@pytest.mark.parametrize("inheritance_name", ["name", "Car", "generic_class",
                                              "long_long_long_long_long_long_long"])
def test_single_inheritance_with_letters_only_and_no_space(inheritance_name):
    inheritance = ClassData(inheritance_name)
    inheritance_to_code = InheritanceToJava([inheritance])
    assert inheritance_to_code.get_formatted() == ' extends ' + inheritance_name


@pytest.mark.parametrize("name_one, name_two", [("Client", "Father"),
                                                ("generic_class", "not_too_long")])
def test_double_inheritance_with_letters_only_and_no_space(name_one, name_two):
    inheritance_one = ClassData(name_one)
    inheritance_two = ClassData(name_two)
    inheritance_to_code = InheritanceToJava([inheritance_one, inheritance_two])
    assert inheritance_to_code.get_formatted() == ' extends ' + name_one + ", " + name_two
