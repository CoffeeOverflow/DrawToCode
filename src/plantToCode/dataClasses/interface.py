from src.plantToCode.dataClasses.visibility import Visibility
from typing import List
from src.plantToCode.dataClasses.method import Method


class Interface:
    def __init__(self, name: str, 
                 methods: List[Method],
                 visibility: Visibility = Visibility.public,     
                 interfaces: List['Interface'] = []):
        
        self.name = name
        self.methods = methods
        self.interfaces = interfaces
        self.visibility = visibility

    def __eq__(self, other: "Interface"):
        cond1 = self.name == other.name
        cond2 = self.methods == other.methods
        cond3 = self.interfaces == other.interfaces
        cond4 = self.visibility == other.visibility

        if cond1 and cond2 and cond3 and cond4:
            return True
        else:
            return False
