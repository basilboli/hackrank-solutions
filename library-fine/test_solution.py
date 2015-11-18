from solution import *

f = open('samples', 'r')

def next_line():
	return f.readline().replace("\n", "")


def read_test (line):
	input_lines = []
	output_lines = []
	if line == "<=":		
		line = next_line()
		while line != "=>":
			input_lines.append(line)
			line = next_line()
		line = next_line()
		while line != "<=" and line != "END":	
			output_lines.append(line)
			line = next_line()		
		
		result = solution(input_lines[0], input_lines[1])
		assert output_lines[0] == result
		return line

def test_solution():
	line = next_line()
	while line: 
		line = read_test(line)	
	f.close()	
