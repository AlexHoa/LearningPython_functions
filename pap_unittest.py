#!usr/local/bin/python3.6
'''Prime, Armstrong and perfect number tester'''

import unittest

# Testing for prime numbers
def prime_numbers(num):
	final= None
	for i in range(2, num):
		if num%i==0:
			print(num, 'is not a prime number')
			final = False
		else:
			final = True
			print(num, 'is a prime number')
		return final

# Testing for Armstrong numbers
# conversion int-string-division/digits
def armstrong(num):
	s = str(num)
	s1=''
	s2=''
	lon = len(s)
	l = [int(i) for i in s]
	s1 = str(num) + " = " + str(l[0]) + '**' + str(lon)
	for j in range(1,lon):
		s2 = s2 + ' + ' + str(l[j]) + '**' + str(lon)
	return s1+s2



# Testing for Perfect numbers
def perfect_numbers(num):
	l=[]
	sum1=0
	result = None
	for i in range(1, num):
		if num%i==0:
			l.append(i)
	for j in l:
		sum1+=j
	if sum1 == num:
		print('perfect number')
		result = True
	else:
		print('not perfect number')
		result = False
	return result

# unit test
class Test(unittest.TestCase):
	# test function for prime numbers	
	def test_prime_numbers(self):
		self.assertEqual(prime_numbers(3),True)
		self.assertEqual(prime_numbers(4),False)
		self.assertEqual(prime_numbers(5),True)
	
	
	# Test function for Armstrong number
	def test_armstrong(self):
		self.assertEqual(armstrong(153), '153 = 1**3 + 5**3 + 3**3')
		self.assertEqual(armstrong(370), '370 = 3**3 + 7**3 + 0**3')


	# Test function for Perfect number
	def test_perfect_numbers(self):
		self.assertEqual(perfect_numbers(1), False)
		self.assertEqual(perfect_numbers(6), True)
		self.assertEqual(perfect_numbers(10), False)
		self.assertEqual(perfect_numbers(28), True)

unittest.main()

