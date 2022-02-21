#record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
record=["Enter uid0606 Gimoi", "Enter uid4567 Prodo", "Leave uid0606", "Enter uid1234 Prodo", "Change uid1234 OhYeah"]

'''
해당 방법 시도 -> 75점 (시간 초과)
def solution(record):
    answer = []
    an={}
    for i in range(len(record)):
        str=record[i].split(" ")
        if str[0]=="Enter":
            for j in range(len(answer)):
                st=answer[j].split("님")
                if str[1]==an[j]:
                    answer[j]=str[2]+"님"+st[1]        
            answer.append(str[2]+"님이 들어왔습니다.")
            an.append(str[1])
        elif str[0]=="Change":
            for j in range(len(answer)):
                st=answer[j].split("님")
                if str[1]==an[j]:
                    answer[j]=str[2]+"님"+st[1]  
        elif str[0]=="Leave":
            for j in range(len(answer)):
                if str[1]==an[j]:
                    id=j
            st=answer[id].split("님")
            answer.append(st[0]+"님이 나갔습니다.")
            an.append(str[1])
    
    return answer
'''

'''
딕셔너리 사용
변경할 때 an 딕셔너리에서 해당 id값을 key로 갖는 value 모두 변경 가능 
                                      -> 해당 부분에서반복문을 사용X -> 시간 초과 해결
'''
def solution(record):
    answer = []
    an={}
    for i in range(len(record)):
        str=record[i].split(" ")
        if str[0]=="Enter" or str[0]=="Change":
            #id가 key 이름이 value
            an[str[1]]=str[2] 
    for i in range(len(record)):   
        str=record[i].split(" ")   
        if str[0]=="Enter":
            answer.append(an[str[1]]+"님이 들어왔습니다.")
        elif str[0]=="Leave":
            answer.append(an[str[1]]+"님이 나갔습니다.")
    return answer
print(solution(record))
