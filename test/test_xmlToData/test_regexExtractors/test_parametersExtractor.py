import pytest

from src.xmlToData.regexExtractors.parametersExtractor import ParametersExtractor


@pytest.mark.parametrize("xml_string", ["+ get_age(): int",
                                        "# add_weight(      ): int",
                                        "- set_height(   ): int"])
def test_extract_empty_parameters_string_list(xml_string):
    list_of_parameters_string = ParametersExtractor.extract_parameters_string(xml_string)
    assert list_of_parameters_string == ['']


@pytest.mark.parametrize("xml_string", ["+ get_age(int number,float real_number): int",
                                        "# add_weight(     int number     ,    float real_number): int",
                                        "- set_height(   int number, float real_number      ): int"])
def test_extract_parameters_string_list_with_and_without_white_spaces(xml_string):
    list_of_parameters_string = ParametersExtractor.extract_parameters_string(xml_string)
    assert list_of_parameters_string == ["int number", "float real_number"]
