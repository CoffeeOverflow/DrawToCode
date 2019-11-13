from src.plantToCode.interface import Interface
from src.plantToCode.attribute import Attribute
from src.plantToCode.method import Method
from src.plantToCode.visibility import Visibility
from src.plantToCode.interfaceToCode import InterfaceToCode

parameter = Attribute("a", "int", Visibility.public)
one_method = Method("method1", "int")
two_method = Method("method2", "float", parameters=[parameter])

methods = [one_method, two_method]
interface = Interface("interface", methods)


def WriteInterface(interface: Interface) -> None:
    interface_to_code = InterfaceToCode()
    content = interface_to_code.convert(interface)
    with open(interface.name.lower(), "w") as interface_file:
        interface_file.write(content)


WriteInterface(interface)
