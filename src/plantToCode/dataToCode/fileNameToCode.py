from abc import ABC, abstractmethod


class FileNameToCode(ABC):
    @abstractmethod
    def get_file_name(self):
        pass
