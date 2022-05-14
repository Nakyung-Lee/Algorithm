N=int(input())

num=[]

for i in range(N):
    num.append(int(input()))

num.sort(reverse=True)

cnt=0
w=0

for i in range(N):
    cnt+=1
    if w<=num[i]*cnt:
        w=num[i]*cnt

print(w)
    
