'''Program that returns True if the word is a palyndrome'''
import unittest
def palyndrome(word):
	l1 = [i for i in word.upper()]
	l2 = l1[:]
	l2.reverse()
	return l1 == l2

# unit test
class Test(unittest.TestCase):	
	def test_palyndrome(self):
		self.assertEqual(palyndrome('ABBA'),True)
		self.assertEqual(palyndrome('SOS'),True)
		self.assertEqual(palyndrome('SOs'),True)
		self.assertEqual(palyndrome('Kayak'),True)
		self.assertEqual(palyndrome('Jean'),False)
		self.assertEqual(palyndrome('Satanoscillatemymetallicsonatas'),True)

unittest.main()
