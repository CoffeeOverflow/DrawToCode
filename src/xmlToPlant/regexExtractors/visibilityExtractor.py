import re
from dataClasses.visibility import Visibility


class VisibilityExtractor:

    @staticmethod
    def extract_visibility(xml_string) -> Visibility:
        types_of_visibilities = {"+": Visibility.public, "-": Visibility.private, "#": Visibility.protected}
        regex = re.compile(r"^\s*.")
        visibility = str(regex.findall(xml_string))[2:-2]
        return types_of_visibilities[visibility.lstrip()]
