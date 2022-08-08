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
  
  ----------------------------------------------
