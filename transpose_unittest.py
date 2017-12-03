'''Write a program containing a function which returns a transposed matrix.
Have it accept non-square matrices as well.
Write a unit test.'''

import unittest

def transpose(M):
	row = len(M[0])
	col = len(M)
	l2 = []
	l3 = []
	for i in range(0,row):
		for j in range(0,col):
			l2.append(M[j][i])
		l3+=[l2]
		l2=[]
	return l3

# unit test
class Test(unittest.TestCase):	
	def test_transpose(self):
		mT1 = ([1,2,3],[4,5,6],[7,8,9])
		mT2 = ([10,11],[12,13],[14,15])
		mT3 = ([20,21,22],[23,24,25])
		self.assertEqual(transpose(mT1),[[1,4,7],[2,5,8],[3,6,9]])
		self.assertEqual(transpose(mT2),[[10,12,14],[11,13,15]])
		self.assertEqual(transpose(mT3),[[20,23],[21,24],[22,25]])

unittest.main()


