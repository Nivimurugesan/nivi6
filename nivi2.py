ss1=int(input())
li=list(map(int,input().split()))
cd=0
for i in range(len(li)-2):
    for j in range(i+1,len(li)-1):
        for n in range(j+1,len(li)):
            if li[i]<li[j]<li[n] and i<j<n:
                cd=cd+1
print(cd)
