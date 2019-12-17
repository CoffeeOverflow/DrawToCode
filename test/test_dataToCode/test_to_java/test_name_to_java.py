import pytest
from src.dataToCode.languages.ToJava.fileNameToJava import FileNameToJava
from src.dataToCode.dataClasses.classData import ClassData
from src.dataToCode.dataClasses.interface import Interface
from src.dataToCode.dataClasses.method import Method


def test_single_name_class():
    class_data = ClassData("Name")
    file_name_java = FileNameToJava(class_data)
    assert "Name.java" == file_name_java.get_file_name()


def test_single_name_interface():
    method = Method("test")
    interface_data = Interface("StrongName", methods=[method])
    file_name_java = FileNameToJava(interface_data)
    assert "StrongName.java" == file_name_java.get_file_name()

