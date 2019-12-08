from dataClasses.interface import Interface
from dataClasses.attribute import Attribute
from dataClasses.method import Method
from dataClasses.visibility import Visibility
from dataToCode.ToJava.interfaceToJava import InterfaceToJava

parameter = Attribute("a", "int", Visibility.public)
one_method = Method("method1", "int")
two_method = Method("method2", "float", parameters=[parameter])

methods = [one_method, two_method]
interface1 = Interface("interface1", methods)
interface2 = Interface("interface2", methods)

interface = Interface("interface", methods, interfaces=[interface1,
                                                        interface2])

def WriteInterface(interface: Interface) -> None:
    interface_to_code = InterfaceToJava()
    content = interface_to_code.convert(interface)
    with open(interface.name.lower(), "w") as interface_file:
        interface_file.write(content)


WriteInterface(interface)
