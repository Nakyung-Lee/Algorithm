def solution(new_id):
    answer = []
    #1단계 대문자 -> 소문자
    for i in range(len(new_id)):
        new_id=new_id.replace(new_id[i],new_id[i].lower())  
        
    #2단계 특수문자 제거
    str="~!@#$%^&*()=+[{]}:?,<>/"
    new_id = ''.join( x for x in new_id if x not in str)
    
    #3단계 반복적인 마침표 제거
    while ('..' in new_id):
        new_id = new_id.replace('..', '.')
    answer=list(new_id)
    
    #4단계 맨 앞 or 맨 마지막 마침표 제거
    if answer[0]=='.':
        answer[0]=''
    if answer[len(answer)-1]=='.':
        answer[len(answer)-1]=''
    answer="".join(answer)
    
    #5단계 빈 문자열이면 a 작성
    if len(answer)==0:
        answer="a"
        
    #6단계 길이가 16이 넘으면 15자리까지만 남기기 + 제거 후 마지막이 마침표면 제거 
    if len(answer)>=16:
        ans=[]
        for i in range(0,15):
            ans.append(answer[i])
        if ans[len(ans)-1]=='.':
            ans[len(ans)-1]=''
        ans="".join(ans)
        return ans
      
    #7단계 길이가 2이하라면 3자리될때까지 마지막 자리 문자 반복
    if len(answer)<=2:
        answer=list(answer)
        while True:
            answer.append(answer[len(answer)-1])
            if len(answer)==3:
                break
        answer="".join(answer)
    return answer
  
  # -----------------------------------------------------------------------------------------------------------
  # 마음에 드는 풀이
  
  def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for i in new_id:
    	if i.isalnum() or i == '-' or i == '_' or i == '.':
            answer += i
    # 2단계 ( + 내 풀이)
    str="~!@#$%^&*()=+[{]}:?,<>/"
    new_id = ''.join( x for x in new_id if x not in str)
    answer+=new_id

    # 3단계
    while ('..' in answer):
        answer = answer.replace('..', '.')
        
    # 4단계
    if answer[0] == '.':
        answer = answer[1:]
    
    if answer != '':
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5단계
    if answer == '':
        answer += 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7단계
    if len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]

    return answer
