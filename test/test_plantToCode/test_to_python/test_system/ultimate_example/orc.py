from i_attack import IAttack
from i_walk import IWalk


class Orc(IAttack, IWalk):

	def __init__(self, name, age):
		self.name = name
		self.__age = age

	def attack(self, damage):
		pass

	def __sleep(self, hours):
		pass

	def walk(self):
		pass
