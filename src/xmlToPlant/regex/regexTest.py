from src.xmlToPlant.regex.XMLCodeExtractor import  XMLCodeExtractor

a = XMLCodeExtractor("+ idade(): int")
print(a.extract_visibility(), a.extract_name(), a.extract_type())
