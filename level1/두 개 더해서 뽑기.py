#내 풀이 
from itertools import combinations  
def solution(numbers):
    answer = []
    nums=list(combinations(numbers,2))
    for num in nums:
        sum=num[0]+num[1]
        if sum not in answer:
            answer.append(sum)
    answer.sort()
    return answer
  
  
#다른 사람 풀이
'''
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
'''
