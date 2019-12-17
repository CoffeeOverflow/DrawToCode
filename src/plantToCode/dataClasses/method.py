from src.plantToCode.dataClasses.visibility import Visibility
from src.plantToCode.dataClasses.modifier import Modifier
from src.plantToCode.dataClasses.attribute import Attribute
from typing import List


class Method:
    def __init__(self, name: str, 
                return_type: str = "void",
                parameters: List[Attribute] = [], 
                visibility: Visibility = Visibility.public,
                modifier: Modifier = Modifier.none):
                
        self.name = name
        self.return_type = return_type
        self.parameters = parameters
        self.visibility = visibility
        self.modifier = modifier

    def __eq__(self, other: "Method"):
        cond1 = self.name == other.name
        cond2 = self.return_type == other.return_type
        cond3 = self.visibility == other.visibility
        cond4 = self.modifier == other.modifier
        cond5 = len(self.parameters) == len(other.parameters)
        
        if not(cond1 and cond2 and cond3 and cond4 and cond5):
            return False
        for x, y in zip(self.parameters, other.parameters):
            if x != y:
                return False
        
        return True

