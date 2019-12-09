from src.plantToCode.dataToCode.interfaceToCode import InterfaceToCode
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataToCode.ToJava.methodToJava import MethodToJava

from typing import List

class InterfaceToJava(InterfaceToCode):
    
    def __init__(self, interface: Interface):
        self.interface = interface
        self.method_to_code = MethodToJava(self.interface.methods, True)

    def convert(self) -> str:
        
        return (f"import java.util.*;\n\n\n"
                f"{self.interface.visibility.name} interface {self.interface.name}"
                f"{self.codeImplementedInterfaces(self.interface.interfaces)} {{\n"
                f"{self.method_to_code.get_formatted_methods()}\n"
                f"}}")

    @staticmethod    
    def codeImplementedInterfaces(interfaces_list: List[Interface]) -> str:
        if len(interfaces_list) > 0:
            interfaces_names = [x.name for x in interfaces_list]
            interfaces_string = ", ".join(interfaces_names)
            result = f" implements {interfaces_string}"
        else:
            result = ""
        return result

