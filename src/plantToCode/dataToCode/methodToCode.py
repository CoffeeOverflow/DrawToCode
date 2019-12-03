from abc import ABC, abstractmethod


class MethodToCode(ABC):
    @abstractmethod
    def get_formatted_methods(self) -> str:
        pass
