from src.plantToCode.visibility import Visibility
from src.plantToCode.modifier import Modifier
from src.plantToCode.attribute import Attribute
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
