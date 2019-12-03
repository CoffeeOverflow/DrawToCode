from src.plantToCode.interface import Interface
from dataToCode.methodToJava import MethodToJava


class InterfaceToJava:
    @staticmethod
    def convert(interface: Interface) -> str:
        method_to_code = MethodToJava(interface.methods, is_from_interface=True)

        interfaces_code = InterfaceToJava.codeImplementedInterfaces(interface.interfaces)
        return (f"{interface.visibility.name} interface {interface.name}"
                f"{interfaces_code} {{\n"
                f"{method_to_code.get_formatted_methods()}\n"
                f"}}")

    @staticmethod
    def codeImplementedInterfaces(interfaces_list: [Interface]) -> str:
        if len(interfaces_list) > 0:
            interfaces_names = [x.name for x in interfaces_list]
            interfaces_string = ", ".join(interfaces_names)
            result = f" implements {interfaces_string}"
        else:
            result = ""
        return result

