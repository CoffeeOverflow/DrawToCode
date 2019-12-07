from dataClasses.visibility import Visibility
from typing import List
from dataClasses.method import Method


class Interface:
    def __init__(self, name: str, 
                 methods: List[Method],
                 visibility: Visibility = Visibility.public,     
                 interfaces: List['Interface'] = []):
        
        self.name = name
        self.methods = methods
        self.interfaces = interfaces
        self.visibility = visibility
