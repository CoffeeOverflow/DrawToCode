from classData import ClassData
from dataToCode.classToCode import ClassToCode
from dataToCode.toPython.methodToPython import MethodToPython


class ClassToPython(ClassToCode):
    def __init__(self, class_data: ClassData):
        self.class_data = class_data
        self.method_to_code = MethodToPython(self.class_data.methods, False)

    def convert(self) -> str:
        return (f"class {self.class_data.name}"
                f"({self.__formatted_inheritances()}):\n"
                f"{self.__formatted_init()}\n"
                f"{self.method_to_code.get_formatted_methods()}")

    def __formatted_init(self) -> str:
        pass_ = '\t\tpass'
        return (f"\tdef __init__(self" + self.__formatted_parameters() + "):\n"
                f"{self.__formatted_assignments() if self.class_data.fields else pass_}\n")

    def __formatted_parameters(self) -> str:
        fields_name = [f"{field.name}"
                       for field in self.class_data.fields]
        return f", {', '.join(fields_name)}" if self.class_data.fields else ""

    def __formatted_assignments(self) -> str:
        class_fields = [f"\t\tself.{field.name} = {field.name}"
                        for field in self.class_data.fields]
        return '\n'.join(class_fields)

    def __formatted_inheritances(self) -> str:
        inheritances = self.class_data.inheritances + self.class_data.implementations
        inheritances_name = [f"{inheritance.name}"
                             for inheritance in inheritances]
        return ', '.join(inheritances_name)
