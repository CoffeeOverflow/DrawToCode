from src.plantToCode.visibility import Visibility
from typing import List
from src.plantToCode.method import Method


class Interface:
    def __init__(self, name: str, 
                 visibility: Visibility,     
                 methods: List[Method],
                 interfaces: List['Interface'] = []):
        
        self.name = name
        self.methods = methods
        self.interfaces = interfaces
        self.visibility = visibility

    def __str__(self):
        brackets = "{}"
        return (f"{self.visibility.name} interface {self.name} {brackets[0]}"
                f"\n{self.__formatted_methods()}\n"
                f"{brackets[1]}")

    def __repr__(self):
        return self.__str__

    def __formatted_methods(self) -> str:
        methods_list = [f"\t{str(method)}" for method in self.methods] 

        return '\n\n'.join(methods_list)

