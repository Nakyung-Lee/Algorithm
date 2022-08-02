def solution(prices):
    answer = [0 for _ in range(len(prices))]     
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            answer[i]+=1
            if prices[i]>prices[j]:
                break
                
    return answer
  
  
  -------------------------------------------------------
  
  #Queue를 이용한 풀이
  
from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer
