import re


class ParametersExtractor:

    @staticmethod
    def extract_parameters_string(xml_string) -> list:
        regex = re.compile('\(.*\)')
        name = str(regex.findall(xml_string))
        unformatted_parameters_string_list = name[3:-3].split(",")
        formatted_parameters_string_list = []
        for parameter in unformatted_parameters_string_list:
            formatted_parameters_string_list.append(parameter.lstrip())
        return formatted_parameters_string_list
