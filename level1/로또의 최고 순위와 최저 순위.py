def solution(lottos, win_nums):
    answer = []
    a=0
    b=0
    rank=6
    for i in range(6):
        if lottos[i] in win_nums:
            a+=1
        if lottos[i]==0:
            b+=1
    if a<2:
        rank=6
    elif a==2:
        rank=5
    elif a==3:
        rank=4
    elif a==4:
        rank=3
    elif a==5:
        rank=2
    else:
        rank=1
    if rank-b<1:
        answer=[1,rank]
    else:
        answer=[rank-b,rank]
    return answer

#lottos=[45, 4, 35, 20, 3, 9]
#win_nums=[20, 9, 3, 45, 4, 35]

#print(solution(lottos,win_nums))
