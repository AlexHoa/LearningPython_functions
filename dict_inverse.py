''' write a python function that assumes a dict as argument.
Create a dict where the values are the keys.
In case of multiple values, make a list of the keys that had the value.
Return the dictionnary'''

def dict_inverse(dict1):
	dict1 = {value:key for key,value in dict1.items()}
	return dict1
