'''Prime, Armstrong and perfect number tester'''

# Testing for prime numbers
def prime_numbers(num):
	for i in range(2, num):
		if num%i==0:
			print(num, 'is not a prime number')
		else: print (num, 'is a prime number')
		return

# Testing for Armstrong numbers
# conversion int-string-division/digits
def armstrong(num):
	s = str(num)
	lon = len(s)
	l = [int(i) for i in s]
	for j in range(lon-1):
		print(num, '=', l[j],'**',lon,'+ ',end='')
	print(l[lon-1], '**',lon)
	return



# Testing for Perfect numbers
def perfect_numbers(num):
	l=[]
	sum1=0
	for i in range(1, num):
		if num%i==0:
			l.append(i)
	for j in l:
		sum1+=j
	if sum1 == num:
		print('perfect number')
	else:print('not perfect number')
	return
