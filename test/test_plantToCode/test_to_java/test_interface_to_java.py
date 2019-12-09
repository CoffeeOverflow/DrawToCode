from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataToCode.ToJava.interfaceToJava import InterfaceToJava
from src.plantToCode.dataClasses.method import Method


def test_convert_interface():
    method = Method("example")
    interface = Interface("interface_example", [method])
    interface_java = InterfaceToJava(interface)
    output = interface_java.convert()
    expected = "import java.util.*;\n\npublic interface interface_example {\n\n\tpublic void example();\n}"
    assert output == expected

def test_convert_interface_wit_implement_interface():
    method = Method("example")
    interface1 = Interface("interface1", [method])
    interface2 = Interface("interface2", [method], interfaces=[interface1])
    interface_java2 = InterfaceToJava(interface2)
    output = interface_java2.convert()
    expected = (f"import java.util.*;\n\npublic interface interface2 " 
                f"implements interface1 {{\n\n\tpublic void example();\n}}")
    assert output == expected

def test_convert_interface_wit_implement_interfacee():
    method = Method("example")
    interface1 = Interface("interface1", [method])
    interface3 = Interface("interface3", [method])
    interface2 = Interface("interface2", [method], interfaces=[interface1,
                                                               interface3])
    interface_java2 = InterfaceToJava(interface2)
    output = interface_java2.convert()
    expected = (f"import java.util.*;\n\npublic interface interface2 " 
                f"implements interface1, interface3 {{\n\n\tpublic void example();\n}}")
    assert output == expected
