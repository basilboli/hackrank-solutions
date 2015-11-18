"""
Sample Input 07:05:45PM
Sample Output 19:05:45
"""
def parse(str):
	return

def convert(hour, ampm):
	if (ampm=="PM"):
		if not hour == "12":
			hour = int(hour) + 12
	elif (ampm=="AM"):
		if hour == "12":
			hour = "00"	
	return hour	

def solution(time):	
	ampm=time[-2:]
	parts=time[:-2].split(":")

	return "%s:%s:%s" % (convert(parts[0], ampm), parts[1], parts[2] )

if __name__ == "__main__":
	time = raw_input()
	print solution(time)











