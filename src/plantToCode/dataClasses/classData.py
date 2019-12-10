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

    def __eq__(self, other: "ClassData"):
        cond1 = self.name == other.name
        cond2 = self.fields == other.fields
        cond3 = self.methods == other.methods
        cond4 = self.inheritances == other.inheritances
        cond5 = self.implementations == other.implementations
        cond6 = self.visibility == other.visibility
        cond7 = self.modifier == other.modifier

        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7:
            return True
        else:
            return False
