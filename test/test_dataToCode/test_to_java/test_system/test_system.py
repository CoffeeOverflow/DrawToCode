import pytest
import os
import filecmp
import subprocess

from src.dataToCode.dataClasses.attribute import Attribute
from src.dataToCode.dataClasses.classData import ClassData
from src.dataToCode.dataClasses.interface import Interface
from src.dataToCode.dataClasses.method import Method
from src.dataToCode.write_files import write_files
from src.dataToCode.dataClasses.visibility import Visibility
from src.dataToCode.dataClasses.modifier import Modifier

def test_strategy_example_java(tmpdir):
    def create_do_algorithm():
        attribute = Attribute("data", "ArrayList<String>")
        method = Method("doAlgorithm", parameters=[attribute],
                        return_type="ArrayList<String>")
        return method

    def create_strategy():
        method = create_do_algorithm()
        strategy = Interface("Strategy", methods=[method])
        return strategy

    def create_context():
        attribute = Attribute("strategy", "Strategy",
                              visibility=Visibility.public)
        method = Method("doSomeBusinessLogic")
        context = ClassData("Context", methods=[method], fields=[attribute])
        return context

    def create_concrete_a():
        method = create_do_algorithm()
        strategy = create_strategy()
        concrete_a = ClassData("ConcreteStrategyA", methods=[method],
                               implementations=[strategy])
        return concrete_a

    def create_concrete_b():
        method = create_do_algorithm()
        strategy = create_strategy()
        concrete_b = ClassData("ConcreteStrategyB", methods=[method],
                               implementations=[strategy])
        return concrete_b

    objects = [create_strategy(), create_context(), create_concrete_a(),
               create_concrete_b()]
    write_files(objects, tmpdir, "java")
    files_path = ["Strategy.java", "Context.java", "ConcreteStrategyA.java",
                  "ConcreteStrategyB.java"]
    strategy_path = os.path.abspath(os.path.join(__file__,
                                                 "../strategy_example"))
    generated_path = [os.path.join(tmpdir, x) for x in files_path]
    truth_path = [os.path.join(strategy_path, x) for x in files_path]

    for truth_file_path, generated_file_path in zip(truth_path,
                                                    generated_path):
        
        print(filecmp.cmp(truth_file_path, generated_file_path))
        assert filecmp.cmp(truth_file_path, generated_file_path)


def test_strategy_xml(tmpdir):

    main_path = os.path.abspath(os.path.join(__file__,"..", "..", "..", "..", "..", "main.py"))
    xml_path = os.path.abspath(os.path.join(__file__,"..", "..", "..", "..", "strategy.xml"))
    subprocess.run(["python3", main_path,
                    f"--xml_file={xml_path}", f"--code_path={tmpdir}",
                    "--language=java"])
    files_path = ["Strategy.java", "Context.java", 
                  "ConcreteStrategyA.java",
                  "ConcreteStrategyB.java"]
    strategy_path = os.path.abspath(os.path.join(__file__,
                                                 "../strategy_example"))
    generated_path = [os.path.join(tmpdir, x) for x in files_path]
    truth_path = [os.path.join(strategy_path, x) for x in files_path]

    for truth_file_path, generated_file_path in zip(truth_path,
                                                    generated_path):
        assert filecmp.cmp(truth_file_path, generated_file_path)

def test_ultimate_example_java(tmpdir):

    def create_spell():
        method = Method("doEffect")
        interface = Interface("ISpell", methods=[method])
        return interface

    def create_food():
        method = Method("getNutrients", return_type="String")
        interface = Interface("IFood", methods=[method])
        return interface

    def create_weapon():
        name = Attribute("name", "String", visibility=Visibility.public)
        age = Attribute("age", "int", visibility=Visibility.private)
        attribute = Attribute("attribute", "Attribute",
                              visibility=Visibility.protected)

        getAttribute = Method("getAttribute", return_type="Attribute")
        setAttribute = Method("setAttribute", return_type="void",
                              parameters=[attribute])
        weapon = ClassData("Weapon", methods=[getAttribute, setAttribute], 
                           fields=[name, age, attribute])
        return weapon

    def create_attribute():
        field1 = Attribute("value", "float", visibility=Visibility.public)
        field2 = Attribute("multiplier", "float", visibility=Visibility.public)
        attribute = ClassData("Attribute", fields=[field1, field2])
        return attribute

    def create_walk():
        method = Method("walk")
        interface = Interface("IWalk", methods=[method])
        return interface
    
    def create_attack():
        damage = Attribute("damage", "int", visibility=Visibility.public)
        method = Method("attack", parameters=[damage])
        interface = Interface("IAttack", methods=[method])
        return interface
    
    def create_orc():
        name = Attribute("name", "String", visibility=Visibility.public)
        age = Attribute("age", "int", visibility=Visibility.private)
        weapon = Attribute("weapon", "Weapon", visibility=Visibility.private)
        damage = Attribute("damage", "int", visibility=Visibility.public)
        hours = Attribute("hours", "int", visibility=Visibility.public)
        
        walk = create_walk()
        attack_interface = create_attack()

        attack_method = Method("attack", parameters=[damage])
        sleep = Method("sleep", parameters=[hours],
                       visibility=Visibility.private)
        walk_method = Method("walk", parameters=[])

        orc = ClassData("Orc", methods=[attack_method, walk_method, sleep],
                        fields=[name, age, weapon],
                        implementations=[attack_interface, walk])
        return orc
    
    def create_high_orc():
        damage = Attribute("damage", "int", visibility=Visibility.public)
        hours = Attribute("hours", "int", visibility=Visibility.public)
        spell = Attribute("spell", "ISpell", visibility=Visibility.protected)

        attack = Method("attack", parameters=[damage],
                        modifier=Modifier.override)
        sleep = Method("sleep", parameters=[hours], 
                       visibility=Visibility.private, 
                       modifier=Modifier.override)

        orc = create_orc()

        high_orc = ClassData("HighOrc", methods=[attack, sleep], 
                             fields=[spell], inheritances=[orc])
        return high_orc
    
    def create_fat_orc():
        food = Attribute("food", "IFood", visibility=Visibility.public)

        eat = Method("eat", parameters=[food])

        orc = create_orc()

        fat_orc = ClassData("FatOrc", methods=[eat],
                            inheritances=[orc])
        return fat_orc
    
    def create_obese_orc():
        food = Attribute("food", "IFood", visibility=Visibility.public)
        heart_attack = Attribute("heartAttackChance", "int",
                                 visibility=Visibility.public)
        
        eat = Method("eat", parameters=[food], modifier=Modifier.override)

        fat_orc = create_fat_orc()

        obese_orc = ClassData("ObeseOrc", methods=[eat], 
                             fields=[heart_attack], inheritances=[fat_orc])
        return obese_orc

    objects = [create_spell(), create_food(), create_weapon(), 
               create_attribute(), create_attack(), create_walk(), 
               create_orc(), create_high_orc(), create_fat_orc(), 
               create_obese_orc()]
    write_files(objects, tmpdir, "java")

    ultimate_path = os.path.abspath(os.path.join(__file__,
                                                 "../ultimate_example"))
    all_files_path = os.listdir(ultimate_path)
    
    files_path = []
    for file_path in all_files_path:
        if file_path.endswith(".java"):
            files_path.append(file_path)

    generated_path = [os.path.join(tmpdir, x) for x in files_path]
    truth_path = [os.path.join(ultimate_path, x) for x in files_path]

    for truth_file_path, generated_file_path in zip(truth_path,
                                                    generated_path):
        assert filecmp.cmp(truth_file_path, generated_file_path)

