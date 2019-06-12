rr=int(input())
ff=[int(i) for i in input().split()]
x=0
for i in range(rr):
	for j in range(i):
		if ff[j]<ff[i]:
			x+=ff[j]
print(x)
