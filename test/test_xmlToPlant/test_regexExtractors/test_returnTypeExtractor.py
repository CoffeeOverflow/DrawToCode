import pytest
from src.xmlToPlant.regexExtractors.returnTypeExtractor import ReturnTypeExtractor


@pytest.mark.parametrize("xml_string", ["- age: int         ", "#        weight:    int       ",
                                        "     +      height:               int"])
def test_extract_type_int_from_attributes(xml_string):
    type_ = ReturnTypeExtractor.extract_type(xml_string)
    assert type_ == "int"


@pytest.mark.parametrize("xml_string", ["- age: float         ", "#        weight:    float       ",
                                        "     +      height:               float"])
def test_extract_type_float_from_attributes(xml_string):
    type_ = ReturnTypeExtractor.extract_type(xml_string)
    assert type_ == "float"


@pytest.mark.parametrize("xml_string", ["- age: List         ", "#        weight:    List       ",
                                        "     +      height:               List"])
def test_extract_type_list_from_attributes(xml_string):
    type_ = ReturnTypeExtractor.extract_type(xml_string)
    assert type_ == "List"


@pytest.mark.parametrize("xml_string", ["- age: void         ", "#        weight:    void       ",
                                        "     +      height:               void"])
def test_extract_type_void_from_attributes(xml_string):
    type_ = ReturnTypeExtractor.extract_type(xml_string)
    assert type_ == "void"


@pytest.mark.parametrize("xml_string", ["+ get_age(): int       ",
                                        "#        add_weight(float additional_weight):         int          ",
                                        "     -      set_height(double height):       int"])
def test_extract_return_type_int_from_methods(xml_string):
    return_type = ReturnTypeExtractor.extract_type(xml_string)
    assert return_type == "int"


@pytest.mark.parametrize("xml_string", ["+ get_age(): void       ",
                                        "#        add_weight(float additional_weight):         void          ",
                                        "     -      set_height(double height):       void"])
def test_extract_return_type_void_from_methods(xml_string):
    return_type = ReturnTypeExtractor.extract_type(xml_string)
    assert return_type == "void"


@pytest.mark.parametrize("xml_string", ["+ get_age(): List       ",
                                        "#        add_weight(float additional_weight):         List          ",
                                        "     -      set_height(double height):       List"])
def test_extract_return_type_list_from_methods(xml_string):
    return_type = ReturnTypeExtractor.extract_type(xml_string)
    assert return_type == "List"


@pytest.mark.parametrize("xml_string", ["+ get_age(): float       ",
                                        "#        add_weight(float additional_weight):         float          ",
                                        "     -      set_height(double height):       float"])
def test_extract_return_type_float_from_methods(xml_string):
    return_type = ReturnTypeExtractor.extract_type(xml_string)
    assert return_type == "float"
