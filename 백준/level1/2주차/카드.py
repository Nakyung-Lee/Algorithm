import sys
n=int(input())

dic={}

for i in range(n):
    num=int(sys.stdin.readline())
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
        
dic=dict(sorted(dic.items(), key=lambda x : x[0]))

print(sorted(dic.items(), key=lambda x : x[1],reverse = True)[0][0])
