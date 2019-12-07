from typing import List
from attribute import Attribute
from visibility import Visibility


class InitToPython:
    def __init__(self, class_fields: List[Attribute]):
        self.class_fields = class_fields
        self.visibility_dict = {Visibility.private: "__",
                                Visibility.protected: "_",
                                Visibility.public: "",
                                Visibility.package: ""}

    def get_formatted(self) -> str:
        pass_ = '\t\tpass'
        return (f"\tdef __init__(self" + self.__formatted_parameters() + "):\n"
                f"{self.__formatted_assignments() if self.class_fields else pass_}\n")

    def __formatted_parameters(self) -> str:
        fields_name = [f"{field.name}"
                       for field in self.class_fields]
        return f", {', '.join(fields_name)}" if self.class_fields else ""

    def __formatted_assignments(self) -> str:
        class_fields = [f"\t\tself.{self.visibility_dict[field.visibility]}"
                        f"{field.name} = {field.name}"
                        for field in self.class_fields]
        return '\n'.join(class_fields)