from random import randint

class Bob:
	def __init__(self, N, g, coprimeList):
		self.N = N
		self.g = g
		self.coprimeList = coprimeList
		self.b = None
		self.gBMod = None
		self.gAMod = None
		self.gABMod = None

	def selectPrivateB(self):
		self.b = self.coprimeList[randint(0, len(self.coprimeList)-1)]
		print("Bob Private: ", self.b)

	def computeGBMod(self):
		self.gBMod = self.g**self.b % self.N
		print("Bob gB: ", self.gBMod)
		return self.gBMod

	def receiveGAMod(self, gAMod):
		self.gAMod = gAMod

	def computeGABMod(self):
		self.gABMod = self.gAMod**self.b % self.N
		print("Bob final: ", self.gABMod)