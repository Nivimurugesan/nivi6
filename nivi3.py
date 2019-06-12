import math
aa=int(input())
bb=math.log10(aa)/math.log10(2)
if math.ceil(bb)==math.floor(bb):
	print(0)
else:
	cc=(aa-1)//2
	dd=cc*2
	print(aa-dd)
