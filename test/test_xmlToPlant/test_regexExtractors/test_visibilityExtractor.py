import pytest
from src.plantToCode.visibility import Visibility
from src.xmlToPlant.regexExtractors.visibilityExtractor import VisibilityExtractor


@pytest.mark.parametrize("xml_string", ["+ age: int", "+        weight: float",
                                        "     +      height: double"])
def test_extract_public_visibility_from_attributes(xml_string):
    visibility = VisibilityExtractor.extract_visibility(xml_string)
    assert visibility == Visibility.public


@pytest.mark.parametrize("xml_string", ["- age: int", "-        weight: float",
                                        "     -      height: double"])
def test_extract_private_visibility_from_attributes(xml_string):
    visibility = VisibilityExtractor.extract_visibility(xml_string)
    assert visibility == Visibility.private


@pytest.mark.parametrize("xml_string", ["# age: int", "#        weight: float",
                                        "     #      height: double"])
def test_extract_protected_visibility_from_attributes(xml_string):
    visibility = VisibilityExtractor.extract_visibility(xml_string)
    assert visibility == Visibility.protected


@pytest.mark.parametrize("xml_string", ["+ get_age(): int", "+        add_weight(float additional_wight): float",
                                        "     +      set_height(double height): void"])
def test_extract_public_visibility_from_methods(xml_string):
    visibility = VisibilityExtractor.extract_visibility(xml_string)
    assert visibility in [Visibility.protected, Visibility.public, Visibility.private]


@pytest.mark.parametrize("xml_string", ["- get_age(): int", "-        add_weight(float additional_wight): float",
                                        "     -      set_height(double height): void"])
def test_extract_private_visibility_from_methods(xml_string):
    visibility = VisibilityExtractor.extract_visibility(xml_string)
    assert visibility in [Visibility.protected, Visibility.public, Visibility.private]


@pytest.mark.parametrize("xml_string", ["# get_age(): int", "#        add_weight(float additional_wight): float",
                                        "     #      set_height(double height): void"])
def test_extract_protected_visibility_from_methods(xml_string):
    visibility = VisibilityExtractor.extract_visibility(xml_string)
    assert visibility in [Visibility.protected, Visibility.public, Visibility.private]
