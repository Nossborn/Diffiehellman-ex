from math import sqrt
from random import randint

from Diffiehellman_Alice import Alice
from Diffiehellman_Bob import Bob

import time

def noCommonPrimeFactor(i, N):
	NPrimeFactors = primeFactors(N) #This doesn't need to be recalculated every time...
	iPrimeFactors = primeFactors(i)
	return len(list(set(NPrimeFactors).intersection(iPrimeFactors))) == 0

def primeFactors(n):
	primeFactors = []
	# Print the number of two's that divide n
	while n % 2 == 0:
		primeFactors.append(2),
		n = n / 2

	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(sqrt(n))+1,2):
		# while i divides n , print i ad divide n
		while n % i== 0:
			primeFactors.append(i),
			n = n / i

	# Condition if n is a prime
	# number greater than 2
	if n > 2:
		primeFactors.append(n)
	return primeFactors

def getGeneratorPeriodList(n, N):
	generatorPeriodList = []
	i = 1
	noOccurrenceOf1 = True
	while noOccurrenceOf1:
		element = (n**i) % N
		generatorPeriodList.append(element)
		if element == 1:
			noOccurrenceOf1 = False
		else:
			i += 1
	return generatorPeriodList


def getCoprimeList(N):
	coprimeList = []
	i = 1
	while i < N:
		if noCommonPrimeFactor(i, N):
			coprimeList.append(i)
		i += 1
	return coprimeList


def findGenerators(N, coprimeList):
	generators = []
	j = 0
	for n in coprimeList:
		r = getGeneratorPeriodList(n, N)
		if len(r) == len(coprimeList):
			generators.append(r[0])
		j += 1
		print("%d of %d in coprime list" % (j,len(coprimeList)))

	if len(generators) == 0:
		print("No generators for: ", N)
		quit()
	print("\n")
	return generators

def selectGenerator(generators):
	i = randint(0, len(generators)-1)
	return generators[i]


def main():
	startTime = time.time()

	N = 11
	print("Number N:\t", N)
	coprimeList = getCoprimeList(N)
	generators = findGenerators(N, coprimeList) # This is very slow
	
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