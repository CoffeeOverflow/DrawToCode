from src.plantToCode.classData import ClassData
from src.plantToCode.interface import Interface
from src.plantToCode.attribute import Attribute
from src.plantToCode.method import Method
from src.plantToCode.visibility import Visibility
from src.plantToCode.modifier import Modifier
from dataToCode.ToJava.classToJava import ClassToJava

attribute1 = Attribute("test", "char", Visibility.private)
attribute2 = Attribute("classy", "Classy", Visibility.package)
class_1 = ClassData("Test")
class_2 = ClassData("Test2")

parameter = Attribute("a", "int", Visibility.public)
one_method = Method("method1", "int", modifier=Modifier.abstract)
two_method = Method("method2", "float", parameters=[parameter])

methods = [one_method, two_method]
interface1 = Interface("in1", methods)
interface2 = Interface("in2", methods)

classy = ClassData("GenericClass", [attribute1, attribute2], [one_method, two_method],
                   inheritances=[class_1], implementations=[interface1, interface2])


def WriteClass(class_data: ClassData) -> None:
    class_to_code = ClassToJava(class_data)
    content = class_to_code.convert()
    with open(class_data.name.lower(), "w") as class_file:
        class_file.write(content)


WriteClass(classy)
