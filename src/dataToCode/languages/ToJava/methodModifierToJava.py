from src.dataToCode.languages.methodModifierToCode import MethodModifierToCode
from src.dataToCode.dataClasses.method import Method
from src.dataToCode.dataClasses.modifier import Modifier


class MethodModifierToJava(MethodModifierToCode):
    def __init__(self, method: Method):
        self.method = method

    def formatted_modifier(self) -> str:
        return f"{self.__get_modifier_value() + self.__get_modifier_space()}"

    def formatted_override(self) -> str:
        if self.method.modifier is Modifier.override:
            return f"@{self.method.modifier.value}\n\t"
        else:
            return ""

    def __get_modifier_value(self) -> str:
        if self.method.modifier is Modifier.override:
            return ''
        else:
            return self.method.modifier.value

    def __get_modifier_space(self) -> str:
        if self.method.modifier in [Modifier.none, Modifier.override]:
            return ''
        else:
            return " "
