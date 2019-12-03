from abc import ABC, abstractmethod


class InterfaceToCode(ABC):
    @abstractmethod
    def convert(self) -> str:
        pass
