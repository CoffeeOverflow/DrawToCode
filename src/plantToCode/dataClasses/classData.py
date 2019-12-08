from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataClasses.visibility import Visibility
from src.plantToCode.dataClasses.modifier import Modifier
from typing import List


class ClassData:
    def __init__(self, name: str,
                 fields: List[Attribute] = [],
                 methods: List[Method] = [],
                 inheritances: List['ClassData'] = [],
                 implementations: List[Interface] = [],
                 visibility: Visibility = Visibility.public,
                 modifier: Modifier = Modifier.none):

        self.name = name
        self.fields = fields
        self.methods = methods
        self.inheritances = inheritances
        self.implementations = implementations
        self.visibility = visibility
        self.modifier = modifier
