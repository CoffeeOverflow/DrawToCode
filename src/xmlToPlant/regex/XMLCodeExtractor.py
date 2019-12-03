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
        regex = re.compile('\s\w+.*:')
        name = str(regex.findall(self.string))
        if('(' in name[3:-3]):
            return str(name[3:-3].split('(')[0])
        return name[3:-3]

    @staticmethod
    def extract_type(self) -> str:
        regex = re.compile('\s\w+$')
        type_ = str(regex.findall(self.string))
        return type_[3:-2]

    @staticmethod
    def extract_parameters(self) -> list:
        regex = re.compile('\(.*\)')
        name = str(regex.findall(self.string))
        unformatted_parameters_list = name[3:-3].split(",")
        formatted_parameters_list = []
        for parameter in unformatted_parameters_list:
            formatted_parameters_list.append(parameter.lstrip())
        return formatted_parameters_list