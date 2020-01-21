from random import randint
import argparse
#from time import time

from Diffiehellman_Alice import Alice
from Diffiehellman_Bob import Bob

from base import getCoprimeList

import db_handler as db

def selectGenerator(generators):
	#Select one at random for now
	i = randint(0, len(generators)-1)
	return generators[i]

def load_generators(N):
	return db.retrieve_generators(N)

def main():
	#startTime = time()
	parser = argparse.ArgumentParser()
	parser.add_argument('-N', dest='seed', type=int, default=0, help="The integer seed for the key exchange")

	N = parser.parse_args().seed

	print("Number N:\t", N)
	coprimeList = getCoprimeList(N)
	#print(time() - startTime)
	#generators = findGenerators(N, coprimeList) # This is very slow
	generators = load_generators(N)
	if(len(generators)==0):
		print("Bad seed! Try again using a different seed.")
		return

	print("Generators:\n" + str(generators))

	g = selectGenerator(generators)
	print("Selected G:\t", g)

	#gTime = time() - startTime
	#print("Generator time:\t", str(round(gTime, 4)) +"s")

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

	#totalTime = time() - startTime
	#print("Key exchange time:\t", str(round(totalTime - gTime, 4)) +"s")
	#print("\nTotal elapsed time:\t", str(round(totalTime, 4)) +"s")

if(__name__ == '__main__'):
	main()