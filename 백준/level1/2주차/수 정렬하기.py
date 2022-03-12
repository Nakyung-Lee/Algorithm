import sys
n=int(sys.stdin.readline())

#input() 시간 초과 해결 -> sys.stdin.readline()

s=[]
for i in range(n):
    num=int(sys.stdin.readline())
    s.append(num)
s.sort()
for i in range(n):
    print(s[i])
