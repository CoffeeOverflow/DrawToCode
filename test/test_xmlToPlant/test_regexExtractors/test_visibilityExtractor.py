import pytest
from src.plantToCode.visibility import Visibility
from src.xmlToPlant.regexExtractors.visibilityExtractor import VisibilityExtractor


@pytest.mark.parametrize("xml_string", ["+ age: int"])
def test_extract_visibility_from_attribute(xml_string):
    visibility = VisibilityExtractor.extract_visibility(xml_string)
    assert visibility in [Visibility.public, Visibility.private, Visibility.protected]


@pytest.mark.parametrize("xml_string", ["# get_age(): int"])
def test_extract_visibility_from_method(xml_string):
    visibility = VisibilityExtractor.extract_visibility(xml_string)
    assert visibility in [Visibility.public, Visibility.private, Visibility.protected]
