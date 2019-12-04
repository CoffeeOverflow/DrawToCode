import re
from src.plantToCode.visibility import Visibility


class VisibilityExtractor:

    @staticmethod
    def extract_visibility(xml_string) -> Visibility:
        types_of_visibilities = {"+": Visibility.public, "-": Visibility.private, "#": Visibility.protected}
        regex = re.compile('^.')
        visibility = str(regex.findall(xml_string))
        return types_of_visibilities[visibility[2:-2]]
