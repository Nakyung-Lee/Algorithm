from itertools import permutations

def sosu(n):
    if n<2:
        return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    num_list=[]
    for i in range(1,len(numbers)+1):
        num_list.extend(permutations(numbers,i))
    nums=[]
    for i in num_list:
        i = int(''.join(i))
        nums.append(i)
    for i in (set(nums)):
        if sosu(i)==1:
            answer+=1
            
    return answer
