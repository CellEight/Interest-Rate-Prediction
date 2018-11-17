def stringTo3TupleList(string):
	"""Takes as input a string and returns a list of all possible 3-tuples of ajacent words"""
	output = []
	string = string.split()
	for i in range(len(string-2)):
		output.append(string[i:i+3])
	return ouput

