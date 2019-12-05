import re


class AttributeNameExtractor:

    @staticmethod
    def extract_name(xml_string) -> str:
        regex = re.compile(r"\w+\(*.*:")
        name = str(regex.findall(xml_string))
        return name[2:-3]
