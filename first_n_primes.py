from math import log1p

class Primes(object):
	"""docstring for Primes"""
	@staticmethod
	def first(number):

		def eratosphene(number):
			multiples = set()
			i = 1
			n = 0
			while n < number + 4:
				n = i/(log1p(i) - 1.0836)
				i += 5
			n = i
			for i in range(2,n):
				if i not in multiples:
					yield i
					multiples.update(range(i*i,n+1,i))
		return list(eratosphene(number))[:number]
			




print(Primes.first(7059)[-9:-4])