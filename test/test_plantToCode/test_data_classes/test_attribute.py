from src.plantToCode.dataClasses.attribute import Attribute
import pytest
from src.plantToCode.dataClasses.visibility import Visibility

testdata = [
 (["a", "int", Visibility.public], ["b", "float", Visibility.private], False),
 (["a", "int", Visibility.public], ["b", "float", Visibility.public], False),
 (["a", "int", Visibility.public], ["b", "int", Visibility.private], False),
 (["a", "int", Visibility.public], ["b", "int", Visibility.public], False),
 (["a", "int", Visibility.public], ["a", "float", Visibility.private], False),
 (["a", "int", Visibility.public], ["a", "float", Visibility.public], False),
 (["a", "int", Visibility.public], ["a", "int", Visibility.private], False),
 (["a", "int", Visibility.public], ["a", "int", Visibility.public], False),
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_attribute_equal(a, b, expected):
    a = Attribute(a[0], a[1], a[2])
    b = Attribute(b[0], b[1], b[2])
    output = (a == b)
    assert output == expected



