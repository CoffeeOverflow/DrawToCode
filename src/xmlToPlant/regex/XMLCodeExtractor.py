import re

class XMLCodeExtractor:
    def __init__(self, string: str):
        self.string = string

    @staticmethod
    def extract_visibility(self) -> str:
        regex = re.compile('^.')
        visibility = str(regex.findall(self.string))
        return visibility[2:-2]

    @staticmethod
    def extract_name(self) -> str:
        regex = re.compile('.\s\w+.*:')
        name = str(regex.findall(self.string))
        return name[4:-3]

    @staticmethod
    def extract_type(self) -> str:
        regex = re.compile('\s\w+$')
        type_ = str(regex.findall(self.string))
        return type_[3:-2]
