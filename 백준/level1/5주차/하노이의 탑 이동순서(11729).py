n=int(input())

# start, mid, end
p=[]

def hanoi(n,a,b,c):
    global cnt
    if n==1:
        p.append([a,c])
        cnt+=1
        return
    else:
        cnt+=1
        hanoi(n-1,a,c,b)
        p.append([a,c])
        hanoi(n-1,b,a,c)
        
cnt=0
hanoi(n,1,2,3)
print(cnt)
for i in range(cnt):
    print(p[i][0], p[i][1])
