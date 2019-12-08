from dataClasses.interface import Interface
from dataClasses.method import Method
from dataClasses.attribute import Attribute
from dataClasses.classData import ClassData
from src.plantToCode.dataToCode.ToJava.classToJava import ClassToJava
from dataClasses.modifier import Modifier
from dataClasses.visibility import Visibility
import os.path as path

examples_folder = path.abspath(
    path.join(__file__, "../../class_examples/java/"))


def test_java_example_1():
    att1 = Attribute("name", "String", Visibility.public)
    att2 = Attribute("age", "int", Visibility.private)

    method1 = Method("bark", "void", [], Visibility.public)
    param1 = Attribute("byAge", "int", Visibility.public)
    method2 = Method("growUp", "bool", [param1], Visibility.private)
    dog_class = ClassData("Dog", [att1, att2], [method1, method2])

    with open(path.join(examples_folder, "java_example_1.txt"), 'r') as java_example:
        expected = java_example.read()

    result = ClassToJava(dog_class).convert()
    assert result == expected


def test_java_example_2():
    param1 = Attribute("damage", "int")
    param2 = Attribute("entity", "Entity")
    param3 = Attribute("bonus", "Bonus")
    method1 = Method("attack", "void", [param1, param2, param3])
    method2 = Method("cry", "void", [], Visibility.protected, Modifier.static)
    orc_class = ClassData("Orc", [], [method1, method2],
                          [ClassData("Monster")], [Interface("IWalk", []), Interface("IAttack", [])])

    with open(examples_folder + "/java_example_2.txt", 'r') as java_example:
        expected = java_example.read()

    result = ClassToJava(orc_class).convert()
    assert result == expected
