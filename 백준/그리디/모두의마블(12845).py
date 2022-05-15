import sys

N=int(input())

num=list(map(int,sys.stdin.readline().split()))
    
num.sort(reverse=True)

lv=num[0]
gold=0

for i in range(1,len(num)) :
    gold+=(lv+num[i])

print(gold)
