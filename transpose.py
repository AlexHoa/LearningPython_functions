'''Write a program containing a function which returns a transposed matrix.
Have it accept non-square matrices as well.
Write a unit test.'''

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
