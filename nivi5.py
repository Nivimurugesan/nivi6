pp,qq=input().split()
pp=int(pp)
qq=int(qq)
def arm(aa):
    aa=str(aa)
    num=len(aa)
    aa=int(aa)
    qq=aa
    ss=0
    tt=0
    for  i in range(0,num):
        tt=aa%10
        tt=tt**3
        ss=ss+tt
        aa=aa//10
    if ss == qq:
        print(qq, end =" ")
for i in range (pp+1,qq):
    arm(i)
