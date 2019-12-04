import re


class XMLCodeExtractor:
    def __init__(self, string: str):
        self.string = string

    @staticmethod
    def extract_visibility(self) -> str:
        regex = re.compile('^.')
        visibility = str(regex.findall(self))
        return visibility[2:-2]

    @staticmethod
    def extract_name(self) -> str:
        regex = re.compile('\w+\(*.*:')
        name = str(regex.findall(self))
        if '(' in name[2:-3]:
            return str(name[2:-3].split('(')[0])
        return name[2:-3]

    @staticmethod
    def extract_type(self) -> str:
        regex = re.compile('\)*:\s*\w+')
        list_of_types = regex.findall(self)
        #print(list_of_types)
        if ')' in list_of_types[-1]:

            return list_of_types[-1].split(':')[1].lstrip()

        return list_of_types[-1][2:].lstrip()


    @staticmethod
    def extract_parameters_string(self) -> list:
        regex = re.compile('\(.*\)')
        name = str(regex.findall(self))
        unformatted_parameters_string_list = name[3:-3].split(",")
        formatted_parameters_string_list = []
        for parameter in unformatted_parameters_string_list:
            formatted_parameters_string_list.append(parameter.lstrip())
        return formatted_parameters_string_list
