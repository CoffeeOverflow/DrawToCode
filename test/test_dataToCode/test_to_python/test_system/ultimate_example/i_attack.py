from abc import ABC, abstractmethod


class IAttack(ABC):

	@abstractmethod
	def attack(self, damage):
		pass
