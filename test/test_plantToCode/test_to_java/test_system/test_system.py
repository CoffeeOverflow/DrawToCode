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

