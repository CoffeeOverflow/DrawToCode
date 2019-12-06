import pytest
from src.xmlToPlant.regexExtractors.methodNameExtractor import MethodNameExtractor


@pytest.mark.parametrize("xml_string", ["+ add_weight(): float       ",
                                        "#        add_weight          (float additional_weight):         List          ",
                                        "     -      add_weight   (double height)    :       int"])
def test_extract_method_name_with_and_without_white_spaces(xml_string):
    method_name = MethodNameExtractor.extract_name(xml_string)
    assert method_name == "add_weight"
