from fat_orc import FatOrc


class ObeseOrc(FatOrc):

	def __init__(self, heartAttackChance):
		self.heartAttackChance = heartAttackChance

	def eat(self, food):
		pass
