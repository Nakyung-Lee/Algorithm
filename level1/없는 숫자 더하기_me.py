def solution(answer):
    sum=0
    for i in range(0,10):
        if i not in numbers:
            sum+=i
    return sum
  
numbers=[1,2,3,4,6,7,8,0]
print(solution(numbers))
