from collections import deque

bridge_length=100
weight=100
truck_weights=[10,10,10,10,10,10,10,10,10,10]

def solution(bridge_length, weight, truck_weights):
    q = deque([0]*bridge_length)
    answer = 0
    #sum(q) 사용 했더니 시간 초과 오류 -> bridge_weight 변수 사용 (다리에 추가할 때만 무게 더하고 다리에서 삭제할 때만 무게 빼서 계산)
    bridge_weight=0
    while q:
        #다리 무게 계산 (q 합)
        bridge_weight-=q.popleft()  
        #계속 0번째 스택 값 삭제    
        answer+=1
        #truck_weights 스택에 차량이 있다면
        if truck_weights:
            #다리 위의 차들 무게 + 새로 들어오는 차량 무게 <= 최대 무게
            if bridge_weight + truck_weights[0] <= weight:       
                #다리 무게 계산 (q 합)
                bridge_weight+=truck_weights[0]
                #스택에 추가 / truck_weights에서는 삭제
                q.append(truck_weights.pop(0))
            else:
                # 다리에 올릴 수 있는 차량이 없다면 0 추가 (전체 다리 길이 유지 하기 위해)
                q.append(0)
    return answer

print(solution(bridge_length,weight,truck_weights))
