# 중복허용(X), 순서의미(O) 인 조합을 import
from itertools import combinations   

'''
combination() 사용 : 중복을 허용하지 않고, 순서 의미가 있는 조합을 리턴해준다.
is_prime_number() 함수에서 반복문을 돌 때 범위를 2~(num//2)+1로 설정
'''

'''소수 판별 함수'''

def is_prime_number(num):
  
    # 끝까지 계산하지 않고 (num//2)+1 까지로 설정   
    for n in range(2, (num//2)+1):      
        if num%n == 0:
             return False
        
    return True
  
def solution(nums):
    answer = 0
    
    '''
    nums배열을 3개씩 조합 후 list로 변경
    '''  
    cmb = list(combinations(nums,3))   
    
    '''
    cmb를 하나씩 가져와 sum한 값을 소수 판별 함수로 넘겨줌
    return 값이 True이면 count(=answer) +1
    '''
    for arr in cmb:
        if is_prime_number(sum(arr)):       
            answer += 1                     
    
    return answer


print(solution([1,2,7,6,4]))
