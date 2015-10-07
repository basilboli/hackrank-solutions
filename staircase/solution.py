n = int(raw_input())
r = range(1, n+1)
for i in r:
	print ''.join(map(lambda x : " ",range(0, n-i))) + ''.join(map(lambda x : "#",range(0, i)))