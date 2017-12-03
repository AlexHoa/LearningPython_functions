'''Program that returns True if the word is a palyndrome'''
def palyndrome(word):
	l1 = [i for i in word.upper()]
	l2 = l1[:]
	l2.reverse()
	return l1 == l2
