from abc import ABC, abstractmethod


class InheritanceToCode(ABC):
    @abstractmethod
    def get_formatted(self) -> str:
        pass
