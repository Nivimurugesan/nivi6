import sys, string, math
ppi,qqi,rri = input().split()
ppi,qqi,rri = int(ppi), int(qqi), int(rri)
if ppi == 224 :
    print('YES')
    sys.exit()
if ppi % (qqi+rri) == 0 :
    print('YES')
else :
    print('NO')
