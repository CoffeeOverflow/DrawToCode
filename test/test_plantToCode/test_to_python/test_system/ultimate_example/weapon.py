class Weapon():

	def __init__(self, name, age, attribute):
		self.name = name
		self.__age = age
		self._attribute = attribute

	def getAttribute(self):
		pass

	def setAttribute(self, attribute):
		pass
