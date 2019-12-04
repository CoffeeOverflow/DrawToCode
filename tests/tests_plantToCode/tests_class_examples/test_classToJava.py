from src.plantToCode.method import Method
from src.plantToCode.attribute import Attribute
from src.plantToCode.classData import ClassData
from src.plantToCode.dataToCode.ToJava.classToJava import ClassToJava
from src.plantToCode.visibility import Visibility

examples_folder = "../class_examples/java/"


def test_java_example_1():
    att1 = Attribute("name", "String", Visibility.public)
    att2 = Attribute("age", "int", Visibility.private)

    method1 = Method("bark", "void", [], Visibility.public)
    param1 = Attribute("byAge", "int", Visibility.public)
    method2 = Method("growUp", "bool", [param1], Visibility.private)
    dog_class = ClassData("Dog", [att1, att2], [method1, method2])

    with open(examples_folder + "java_example_1.txt", 'r') as java_example:
        expected = java_example.read()

    result = ClassToJava(dog_class).convert()
    assert result == expected
