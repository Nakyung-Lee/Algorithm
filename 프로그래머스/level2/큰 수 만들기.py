from itertools import combinations

def solution(number, k):
    answer = ''
    
    combi = list(combinations(list(number), len(number)-k))
    
    #print(combi)

    #print(sorted(combi,reverse=True))

    answer = ''.join(sorted(combi,reverse=True)[0])
    
    return answer

  ----------------------------------------------
  #시간초과 발생
  
  #stack 사용 pop
  ----------------------------------------------

def solution(number, k):
    answer = [] # Stack 
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)
