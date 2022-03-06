def solution(numbers, hand):
    answer = ''
    keypad=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left=[3,0]
    right=[3,2]
    a=0
    for k in range(len(numbers)):
        for i in range(4):  
            if numbers[k] == keypad[i][0]:
                answer+='L'
                left=[i,0]
            elif numbers[k] == keypad[i][2]:
                answer+='R'
                right=[i,2]   
            elif numbers[k] == keypad[i][1]:
                if abs(i-left[0]) + abs(1-left[1])<abs(i-right[0]) + abs(1-right[1]):
                    answer+='L'
                    left=[i,1]
                elif abs(i-left[0]) + abs(1-left[1])>abs(i-right[0]) + abs(1-right[1]):
                    answer+='R'
                    right=[i,1] 
                else:
                    if hand=="left":
                        answer+='L'
                        left=[i,1] 
                    if hand=="right":
                        answer+='R'
                        right=[i,1]                
    return answer
