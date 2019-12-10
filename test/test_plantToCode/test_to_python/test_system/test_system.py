import pytest
import os
import filecmp

from src.plantToCode.dataClasses.attribute import Attribute
from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataClasses.method import Method
from src.plantToCode.write_files import write_files
from src.plantToCode.dataClasses.visibility import Visibility


def test_strategy_example(tmpdir):

    def create_do_algorithm():
        attribute = Attribute("data", "str")
        method = Method("do_algorithm", parameters=[attribute])
        return method

    def create_strategy():
        method = create_do_algorithm()
        strategy = Interface("Strategy", methods=[method])
        return strategy

    def create_context():
        attribute = Attribute("strategy", "Strategy", 
                              visibility=Visibility.public)
        method = Method("do_some_business_logic")
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
    write_files(objects, tmpdir, "python")
    files_path = ["strategy.py", "context.py", "concrete_strategy_a.py",
                  "concrete_strategy_b.py"]
    strategy_path = os.path.abspath(os.path.join(__file__,
                                                 "../strategy_example"))
    generated_path = [os.path.join(tmpdir, x) for x in files_path]
    truth_path = [os.path.join(strategy_path, x) for x in files_path]

    for truth_file_path, generated_file_path in zip(truth_path,
                                                    generated_path):
        assert filecmp.cmp(truth_file_path, generated_file_path)
    

def test_ultimate_example(tmpdir):

    def create_spell():
        method = Method("doEffect")
        interface = Interface("ISpell", methods=[method])
        return interface

    def create_food():
        method = Method("getNutrients", return_type="str")
        interface = Interface("IFood", methods=[method])
        return interface

    def create_weapon():
        name = Attribute("name", "str", visibility=Visibility.public)
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
        method = Method("method")
        field = Attribute("field", "Type", visibility=Visibility.public)
        attribute = ClassData("Attribute", methods=[method],
                               fields=[field])
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
        name = Attribute("name", "str", visibility=Visibility.public)
        age = Attribute("age", "int", visibility=Visibility.private)
        damage = Attribute("damage", "int", visibility=Visibility.public)
        hours = Attribute("hours", "int", visibility=Visibility.public)
        
        walk = create_walk()
        attack_interface = create_attack()

        attack_method = Method("attack", parameters=[damage])
        sleep = Method("sleep", parameters=[hours],
                       visibility=Visibility.private)

        orc = ClassData("Orc", methods=[attack_method, sleep], 
                        fields=[name, age], 
                        implementations=[attack_interface, walk])
        return orc
    
    def create_high_orc():
        damage = Attribute("damage", "int", visibility=Visibility.public)
        hours = Attribute("hours", "int", visibility=Visibility.public)
        spell = Attribute("spell", "ISpell", visibility=Visibility.public)

        attack = Method("attack", parameters=[damage])
        sleep = Method("sleep", parameters=[hours], 
                       visibility=Visibility.private)

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
        
        eat = Method("eat", parameters=[food])

        fat_orc = create_fat_orc()

        obese_orc = ClassData("ObeseOrc", methods=[eat], 
                             fields=[heart_attack], inheritances=[fat_orc])
        return obese_orc

    objects = [create_spell(), create_food(), create_weapon(), 
               create_attribute(), create_attack(), create_walk(), 
               create_orc(), create_high_orc(), create_fat_orc(), 
               create_obese_orc()]
    write_files(objects, tmpdir, "python")

    ultimate_path = os.path.abspath(os.path.join(__file__,
                                                 "../ultimate_example"))
    all_files_path = os.listdir(ultimate_path)
    
    files_path = []
    for file_path in all_files_path:
        if file_path.endswith(".py"):
            files_path.append(file_path)

    generated_path = [os.path.join(tmpdir, x) for x in files_path]
    truth_path = [os.path.join(ultimate_path, x) for x in files_path]

    for truth_file_path, generated_file_path in zip(truth_path,
                                                    generated_path):
        assert filecmp.cmp(truth_file_path, generated_file_path)
