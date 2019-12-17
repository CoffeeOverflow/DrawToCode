import re


class ReturnTypeExtractor:

    @staticmethod
    def extract_type(xml_string) -> str:
        regex = re.compile(r"\)*:\s*\w+\<*\w*\>*")
        list_of_types = regex.findall(xml_string)

        if ')' in list_of_types[-1]:
            return list_of_types[-1].split(':')[1].lstrip()

        return list_of_types[-1][1:].lstrip()
