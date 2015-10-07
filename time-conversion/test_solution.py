from solution import *

def test_solution():
	f = open('samples', 'r')
	data = f.read()
	for i in data.split("<="):
		if i:
			actual, expected = map(lambda x : x.replace("\n", ""), i.split("=>"))
			print "Actual   : ", actual
			print "Expected : ", expected
			result = solution(actual)
			print "Solution : ", result		
			assert expected == result

