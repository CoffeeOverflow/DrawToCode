from src.plantToCode.dataClasses.visibility import Visibility

visibility_to_python = {Visibility.private: "__",
                        Visibility.protected: "_",
                        Visibility.public: "",
                        Visibility.package: ""}
