import re


class VisibilityExtractor:

    @staticmethod
    def extract_visibility(xml_string) -> str:
        regex = re.compile('^.')
        visibility = str(regex.findall(xml_string))
        return visibility[2:-2]
