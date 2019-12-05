from src.plantToCode.method import Method
from src.plantToCode.modifier import Modifier


class MethodModifierToJava:
    def __init__(self, method: Method):
        self.method = method

    def get_override_value(self):
        if self.method.modifier is Modifier.override:
            return f"@{self.method.modifier.value}\n\t"
        else:
            return ""

    def get_modifier_value(self):
        if self.method.modifier is Modifier.override:
            return ''
        else:
            return self.method.modifier.value

    def get_modifier_space(self):
        if self.method.modifier in [Modifier.none, Modifier.override]:
            return ''
        else:
            return " "
