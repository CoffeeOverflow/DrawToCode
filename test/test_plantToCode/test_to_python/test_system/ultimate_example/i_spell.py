from abc import ABC, abstractmethod


class ISpell(ABC):

	@abstractmethod
	def doEffect(self):
		pass
