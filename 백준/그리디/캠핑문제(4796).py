import sys

i=0

while(1):
    cnt=0
    s=list(map(int,sys.stdin.readline().split()))
    
    if s[0] == 0 and s[1] == 0 and s[2] == 0:
        break
    i+=1
    
    a = s[2]//s[1]
    
    b = min(s[2]%s[1],s[0])
   
    print("Case "+str(i)+":"+" "+str(s[0]*a+b))
    
