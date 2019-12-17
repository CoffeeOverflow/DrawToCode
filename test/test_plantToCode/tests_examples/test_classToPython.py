from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.languages.toPython.classToPython import ClassToPython
from src.plantToCode.dataClasses.modifier import Modifier
from src.plantToCode.dataClasses.visibility import Visibility
import os.path as path

examples_folder = path.abspath(
    path.join(__file__, "../../code_examples/python/"))


def test_python_example_1():
    att1 = Attribute("name", "String", Visibility.public)
    att2 = Attribute("age", "int", Visibility.private)

    method1 = Method("bark", "void", [], Visibility.public)
    param1 = Attribute("by_age", "int", Visibility.public)
    method2 = Method("grow_up", "bool", [param1], Visibility.private)
    dog_class = ClassData("Dog", [att1, att2], [method1, method2])

    with open(path.join(examples_folder, "python_example_1.txt"), 'r') as python_example:
        expected = python_example.read()

    result = ClassToPython(dog_class).convert()
    assert result == expected


def test_python_example_2():
    param1 = Attribute("damage", "int")
    param2 = Attribute("entity", "Entity")
    param3 = Attribute("bonus", "Bonus")
    method1 = Method("attack", "void", [param1, param2, param3])
    method2 = Method("cry", "void", [], Visibility.protected, Modifier.static)
    orc_class = ClassData("Orc", [], [method1, method2],
                          [ClassData("Monster")], [Interface("IWalk", []), Interface("IAttack", [])])

    with open(examples_folder + "/python_example_2.txt", 'r') as python_example:
        expected = python_example.read()

    result = ClassToPython(orc_class).convert()
    assert result == expected


def test_python_example_3():
    field1 = Attribute("mail_reader", "MailReader", Visibility.public)
    field2 = Attribute("configs", "Configs", Visibility.private)
    field3 = Attribute("network_adapter", "NetworkAdapter", Visibility.public)
    field4 = Attribute("test_runner", "TestRunner", Visibility.protected)

    param1 = Attribute("how_much", "int")
    param2 = Attribute("flag1", "bool")
    param3 = Attribute("flag2", "bool")

    method1 = Method("initialize", "void")
    method2 = Method("initialize_2", "void", modifier=Modifier.abstract)
    method3 = Method("do_things", "void", [param1, param2, param3],
                     Visibility.protected, Modifier.static)
    method4 = Method("no_one_will_ever_use_this", "string",
                     [Attribute("trash", "void"), Attribute("trash_can", "void")],
                     Visibility.private)

    weird_god_class = ClassData("WeirdGodClass", [field1, field2, field3, field4],
                                [method1, method2, method3, method4], [],
                                [Interface("IDoManyThings", [])])

    with open(examples_folder + "/python_example_3.txt", 'r') as python_example:
        expected = python_example.read()

    result = ClassToPython(weird_god_class).convert()
    assert result == expected


def test_python_example_4():
    att1 = Attribute("m", "String", Visibility.public)

    method = Method("v", "void", [], Visibility.public, modifier=Modifier.abstract)
    dog_class = ClassData("Test4", [att1], [method])

    with open(path.join(examples_folder, "python_example_4.txt"), 'r') as python_example:
        expected = python_example.read()

    result = ClassToPython(dog_class).convert()
    assert result == expected
