import re


class MethodNameExtractor:

    @staticmethod
    def extract_name(xml_string) -> str:
        regex = re.compile(r"\w+\s*\(")
        name = str(regex.findall(xml_string))[2:-3].strip()
        return name
