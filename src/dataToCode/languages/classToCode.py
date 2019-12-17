from abc import ABC, abstractmethod


class ClassToCode(ABC):
    @abstractmethod
    def convert(self) -> str:
        pass
