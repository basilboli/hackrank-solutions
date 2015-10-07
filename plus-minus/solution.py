n = int(raw_input())
arr = []
arr = map(int, raw_input().split())
sum_pos=0
sum_neg=0
sum_zero=0

for i in arr:
	if i > 0:
		print "sum_pos"
		sum_pos+=1
	elif i < 0:
		print "sum_neg"
		sum_neg+=1
	else:
		print "sum_zero"
		sum_zero+=1
    
print "%.3f" % (sum_pos/float(n))
print "%.3f" % (sum_neg/float(n))
print "%.3f" % (sum_zero/float(n))