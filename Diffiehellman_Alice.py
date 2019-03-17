from random import randint

class Alice:
	def __init__(self, N, g, coprimeList):
		self.N = N
		self.g = g
		self.coprimeList = coprimeList
		self.a = None
		self.gBMod = None
		self.gAMod = None
		self.gABMod = None

	def selectPrivateA(self):
		self.a = self.coprimeList[randint(0, len(self.coprimeList)-1)]
		print("Alice Private: ", self.a)

	def computeGAMod(self):
		self.gAMod = self.g**self.a % self.N
		print("Alice gB: ", self.gAMod)
		return self.gAMod

	def receiveGBMod(self, gAMod):
		self.gAMod = gAMod

	def computeGABMod(self):
		self.gABMod = self.gAMod**self.a % self.N
		print("Alice final: ", self.gABMod)