from math import sqrt

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
		#print("%d of %d in coprime list" % (j,len(coprimeList)))
	return generators
