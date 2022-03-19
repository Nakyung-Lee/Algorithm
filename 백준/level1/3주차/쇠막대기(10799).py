str=list(input())
stack=[]
cnt=0

for i in range(len(str)):
    if str[i]=='(':
        stack.append('(')
        
    #')'이 나오면
    else:
        if str[i-1]=='(':
            cnt+=len(stack)-1
            stack.pop()
        else:
            cnt+=1
            stack.pop()
            
print(cnt)
