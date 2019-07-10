from random import randint
import time

from diffiehellman_Alice import Alice
from diffiehellman_Bob import Bob

from base import getCoprimeList

import db_handler as db

def selectGenerator(generators):
	#Select one at random for now
	i = randint(0, len(generators)-1)
	return generators[i]

def load_generators(N):
	return db.retrieve_generators(N)

def main():
	startTime = time.time()

	N = 998
	print("Number N:\t", N)
	coprimeList = getCoprimeList(N)
	print(time.time() - startTime)
	#generators = findGenerators(N, coprimeList) # This is very slow
	generators = load_generators(N)

	print("Generators:\n" + str(generators))

	g = selectGenerator(generators)
	print("Selected G:\t", g)

	gTime = time.time() - startTime
	print("Generator time:\t", str(round(gTime, 4)) +"s")

	alice = Alice(N, g, coprimeList)
	bob = Bob(N, g, coprimeList)

	alice.selectPrivateA()
	gAMod = alice.computeGAMod()
	bob.selectPrivateB()
	gBMod = bob.computeGBMod()

	alice.receiveGBMod(gBMod)
	bob.receiveGAMod(gAMod)

	alice.computeGABMod()
	bob.computeGABMod()

	totalTime = time.time() - startTime
	print("Key exchange time:\t", str(round(totalTime - gTime, 4)) +"s")
	print("\nTotal elapsed time:\t", str(round(totalTime, 4)) +"s")

if(__name__ == '__main__'):
	main()