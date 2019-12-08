import pytest
from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.visibility import Visibility
from src.plantToCode.dataToCode.toPython.initToPython import InitToPython


def test_no_attributes_init():
    expected = "\tdef __init__(self):\n\t\tpass\n"
    assert InitToPython([]).get_formatted() == expected


def test_init_with_one_private_attribute():
    att = Attribute("example", "void")
    expected = f"\tdef __init__(self, example):" \
               f"\n\t\tself.__example = example\n"
    assert InitToPython([att]).get_formatted() == expected


def test_init_with_two_public_attributes():
    att1 = Attribute("example1", "void", Visibility.public)
    att2 = Attribute("example2", "void", Visibility.public)
    expected = (f"\tdef __init__(self, example1, example2):"
                f"\n\t\tself.example1 = example1"
                f"\n\t\tself.example2 = example2\n")
    assert InitToPython([att1, att2]).get_formatted() == expected


def test_init_with_three_attributes_with_different_visibilities():
    att1 = Attribute("example1", "void", Visibility.public)
    att2 = Attribute("example2", "void", Visibility.protected)
    att3 = Attribute("example3", "void", Visibility.private)
    expected = (f"\tdef __init__(self, example1, example2, example3):"
                f"\n\t\tself.example1 = example1"
                f"\n\t\tself._example2 = example2"
                f"\n\t\tself.__example3 = example3\n")
    assert InitToPython([att1, att2, att3]).get_formatted() == expected
