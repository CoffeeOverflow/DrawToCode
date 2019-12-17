import pytest

from src.dataToCode.dataClasses.classData import ClassData
from src.dataToCode.dataClasses.interface import Interface
from src.dataToCode.languages.toPython.fileNameToPython import FileNameToPython

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
