import pytest

from src.xmlToData.regexExtractors.attributeNameExtractor import AttributeNameExtractor


@pytest.mark.parametrize("xml_string", ["-      age       :  int         ",
                                        "# age:    float       ",
                                        "     +      age    :               string"])
def test_extract_attribute_name_with_and_without_white_spaces(xml_string):
    attribute_name = AttributeNameExtractor.extract_name(xml_string)
    assert attribute_name == "age"
