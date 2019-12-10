from abc import ABC, abstractmethod


class IWalk(ABC):

	@abstractmethod
	def walk(self):
		pass
