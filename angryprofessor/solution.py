def solution(n, k, a):		
	print "NO" if (len(filter (lambda x : x <=0, a)) >= k ) else "YES"

if __name__ == "__main__":
	t = int(raw_input())
	for i in range(t): 
		n,k = map(int, raw_input().split())
		a = map(int, raw_input().split())
		solution(n, k , a)








