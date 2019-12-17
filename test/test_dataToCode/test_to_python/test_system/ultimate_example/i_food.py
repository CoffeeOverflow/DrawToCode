from abc import ABC, abstractmethod


class IFood(ABC):

	@abstractmethod
	def getNutrients(self):
		pass
