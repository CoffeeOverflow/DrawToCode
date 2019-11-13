from src.plantToCode.interface import Interface
from src.plantToCode.attribute import Attribute
from src.plantToCode.method import Method
from src.plantToCode.visibility import Visibility
from src.plantToCode.modifier import Modifier
from typing import List

parameter = Attribute("a", "int", Visibility.public)
one_method = Method("method1", "int")
two_method = Method("method2", "float", parameters=[parameter])

methods = [one_method, two_method]
interface = Interface("interface", methods)


class InterfaceToCode:
    
    def convert(self, interface: Interface) -> str:
        return (f"{interface.visibility.name} interface {interface.name} {{\n"
                f"{self.__formatted_methods(interface.methods)}\n"
                f"}}")

    def __convert_attribute(self, attribute: Attribute) -> str:
        return (f"{attribute.type_} {attribute.name}")

    def __convert_method(self, method: Method) -> str:
        return (f"{method.visibility.name} "
                f"{method.modifier.name}"
                f"{'' if method.modifier.name is Modifier.none else ' '}"
                f"{method.return_type} {method.name}"
                f"({self.__formatted_parameters(method.parameters)})")

    def __formatted_parameters(self, parameters: List[Attribute]) -> str:
        parameters = [self.__convert_attribute(parameter)
                      for parameter in parameters]
        return ', '.join(parameters)

    def __formatted_methods(self, methods: List[Method]) -> str:
        methods_str_list = [f"\t{self.__convert_method(method)};" 
                            for method in methods] 

        return '\n\n'.join(methods_str_list)




def WriteInterface(interface: Interface) -> None:
    interface_to_code = InterfaceToCode()
    content = interface_to_code.convert(interface)
    with open(interface.name.lower(), "w") as interface_file:
        interface_file.write(content)


WriteInterface(interface)
