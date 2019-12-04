from src.xmlToPlant.regex.xmlCodeExtractor import  XMLCodeExtractor

a = XMLCodeExtractor("+ idade(string, double): int")
print(a.extract_visibility(), a.extract_name(), a.extract_type(), a.extract_parameters())
