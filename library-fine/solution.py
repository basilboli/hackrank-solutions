def f1 (i):
	return i if i > 0 else 0

def f2 (i):
	return 1 if i > 0 else 0

def calculate_fine(actual_date, expected_date):		

	actual_d, actual_m, actual_y = map(int, actual_date.split())
	expected_d, expected_m, expected_y = map(int, expected_date.split())

	# return 10000 * (actual_y - expected_y) + 500 * (actual_m - expected_m) + 15 * (actual_d - expected_d)
	if actual_y == expected_y:
		if actual_m == expected_m:
			if actual_d == expected_d:
				return 0
			else:
				return 15 * f1(actual_d - expected_d)
		else:
			return 500 * f1(actual_m - expected_m)		 
	else:
		return 10000 * f2(actual_y - expected_y)

def solution(actual_date, expected_date):		
	return str(calculate_fine(actual_date, expected_date))

if __name__ == "__main__":
	_input1 = raw_input()
	_input2 = raw_input()
	print solution(_input1, _input2)











