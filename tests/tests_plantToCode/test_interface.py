import sys
sys.path.append("../../")
from src.plantToCode.interface import Interface
from src.plantToCode.method import Method
from src.plantToCode.attribute import Attribute
from src.plantToCode.visibility import Visibility

if __name__ == "__main__":

    one_method = Method("method1", "int")
    parameter = Attribute("a", "int", "private")
    two_method = Method("method2", "float", parameters=[parameter],
                        visibility=Visibility.private)
    
    methods = [one_method, two_method]
    interface = Interface("interface", Visibility.public, methods)
    print(interface._Interface__formatted_methods())
    print()
    print(interface)

