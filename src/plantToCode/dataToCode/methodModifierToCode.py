from abc import ABC, abstractmethod


class MethodModifierToCode(ABC):
    @abstractmethod
    def formatted_modifier(self) -> str:
        pass

    @abstractmethod
    def formatted_override(self) -> str:
        pass
