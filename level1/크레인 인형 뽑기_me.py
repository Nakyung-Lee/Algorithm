
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

def solution(board, moves):
    stack=[]
    answer = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if j+1==moves[i]:
                for k in range(len(board)):
                    if board[k][j]!=0:
                        stack.append(board[k][j])
                        board[k][j]=0
                        if len(stack)>=2 and stack[-1]==stack[-2]:
                            stack.pop()
                            stack.pop()
                            answer+=1
                        break
    return answer*2

'''
def solution(board, moves):
    stack=[]
    answer = 0
    
    # for i in moves
    
    for i in moves:      
        for j in range(len(board)):
        
            # j // i
            
            if j+1==i:
                if board[j][i-1] != 0:
                    stack.append(board[j][i-1])
                    board[j][i-1]=0
                    if len(stack)>=2 and stack[-1]==stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer+=2
                    break
    return answer

'''
print(solution(board,moves))
