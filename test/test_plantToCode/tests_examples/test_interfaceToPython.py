from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataToCode.toPython.interfaceToPython import InterfaceToPython
from src.plantToCode.dataClasses.visibility import Visibility
import os.path as path

examples_folder = path.abspath(
    path.join(__file__, "../../code_examples/python/"))


def test_interface_example_1():
    method1 = Method("do", "void", [], Visibility.public)
    example = Interface("Example", [method1])

    with open(path.join(examples_folder, "interface_example_1.txt"), 'r') as python_example:
        expected = python_example.read()

    result = InterfaceToPython(example).convert()
    assert result == expected


def test_interface_example_2():
    method1 = Method("foo", "void",
                     [Attribute("a", "void"), Attribute("b", "int")],
                     Visibility.public)
    method2 = Method("do", "void", [], Visibility.public)
    example = Interface("Example", [method1, method2],
                        Visibility.public, [Interface("IFoo", [])])

    with open(path.join(examples_folder, "interface_example_2.txt"), 'r') as python_example:
        expected = python_example.read()

    result = InterfaceToPython(example).convert()
    assert result == expected
