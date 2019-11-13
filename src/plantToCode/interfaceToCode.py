from src.plantToCode.interface import Interface
from src.plantToCode.methodToCode import MethodToCode

class InterfaceToCode:
    @staticmethod
    def convert(interface: Interface) -> str:
        method_to_code = MethodToCode(interface.methods)

        return (f"{interface.visibility.name} interface {interface.name} {{\n"
                f"{method_to_code.get_formatted_methods()}\n"
                f"}}")