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
