from dataClasses.attribute import Attribute
from dataClasses.method import Method
from dataClasses.interface import Interface
from dataClasses.visibility import Visibility
from dataClasses.modifier import Modifier
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
