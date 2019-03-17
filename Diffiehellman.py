from math import sqrt
from random import randint

from Diffiehellman_Alice import Alice
from Diffiehellman_Bob import Bob

import time

def noCommonPrimeFactor(i, N):
	NPrimeFactors = primeFactors(N)
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

def genPeriod(n, N):
	genPeriodList = []
	i = 1
	noOccurrenceOf1 = True
	while noOccurrenceOf1:
		element = (n**i) % N
		genPeriodList.append(element)
		if element == 1:
			noOccurrenceOf1 = False
		elif i > 500:
			break
		i = i+1
	return genPeriodList


def findGs(N):
	coprimeList = []
	i = 1
	while i < N:
		if noCommonPrimeFactor(i, N):
			coprimeList.append(i)
		i = i + 1

	gCoprimesLists = []
	for n in coprimeList:
		r = genPeriod(n, N)
		if len(r) == N-1:
			gCoprimesLists.append(r)

	if len(gCoprimesLists) == 0:
		print("No generators for: ", N)
		quit()
	return gCoprimesLists, coprimeList

def selectG(gLists):
	i = randint(0, len(gLists)-1)
	return gLists[i][0]

startTime = time.time()

N = 10007
print("N: ", N)
findGsRes = findGs(N) #Contains the generator numbers period list
gLists = findGsRes[0]
coprimeList = findGsRes[1]
print(gLists)
g = selectG(gLists)
print("G: ", g)

print("Basics time: ", time.time() - startTime)

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

print("End time: ", time.time() - startTime)