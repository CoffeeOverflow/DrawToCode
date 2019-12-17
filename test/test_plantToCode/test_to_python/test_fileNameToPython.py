import pytest

from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.languages.toPython.fileNameToPython import FileNameToPython

data = [
    ("Orc", "orc.py"),
    ("HighOrc", "high_orc.py"),
    ("PrettyLongClassName", "pretty_long_class_name.py")
]


@pytest.mark.parametrize("data_name, expected", data)
def test_file_names_with_class(data_name, expected):
    assert FileNameToPython(ClassData(data_name)).get_file_name() == expected

@pytest.mark.parametrize("data_name, expected", data)
def test_file_names_with_interface(data_name, expected):
    assert FileNameToPython(Interface(data_name, [])).get_file_name() == expected
