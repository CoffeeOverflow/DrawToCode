from dataClasses.interface import Interface
from src.plantToCode.dataToCode.ToJava.interfaceToJava import InterfaceToJava
from dataClasses.method import Method


def test_implemented_interface():
    method = Method("example")
    interface_name = "interface_name"
    interface = Interface(interface_name, [method])
    output = InterfaceToJava.codeImplementedInterfaces([interface])
    assert output == f" implements {interface_name}"


def test_implemented_interfaces():
    method = Method("example")
    interface_name1 = "interface_name1" 
    interface_name2 = "interface_name2" 
    interface1 = Interface(interface_name1, [method])
    interface2 = Interface(interface_name2, [method])
    output = InterfaceToJava.codeImplementedInterfaces([interface1,
                                                        interface2])
    assert output == f" implements {interface_name1}, {interface_name2}"


def test_no_implemented_interfaces():
    output = InterfaceToJava.codeImplementedInterfaces([])
    assert output == ""


def test_convert_interface():
    method = Method("example")
    interface = Interface("interface_example", [method])
    output = InterfaceToJava.convert(interface)
    expected = "public interface interface_example {\n\tpublic void example();\n}"
    assert output == expected

