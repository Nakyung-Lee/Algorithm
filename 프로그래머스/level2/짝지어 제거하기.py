def solution(s):
    answer = -1
    s=list(s)
    
    i=0
    while True:
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            i=0
        else:
            i+=1
        if i==len(s)-1 or len(s)==0:
            break
    if len(s)==0:
        answer=1
    else:
        answer=0
    return answer
  
  -----------------------------------
  시간초과 발생
  변경한 코드 
  --------------------------------
  
  def solution(s):
    answer = -1
    stack=[]
    
    for i in s:
        if stack==[]:
            stack.append(i)
        elif stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
        if len(stack)==0:
            answer=1
        else:
            answer=0
        
    return answer
