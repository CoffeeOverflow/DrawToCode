import re


class MethodNameExtractor:

    @staticmethod
    def extract_name(xml_string) -> str:
        regex = re.compile(r"\w+\(*.*:")
        name = str(regex.findall(xml_string))
        return str(name[2:-3].split('(')[0])
