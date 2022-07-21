def solution(phone_book):
    answer = True
    phone_book.sort()
    i=0
    
    for i in range(len(phone_book)-1):
        st = phone_book[i]
        for st in (phone_book[i+1:]):
            if phone_book[i] == st[:len(phone_book[i])]:
                answer = False
                break
        i+=1
        
    return answer
  
  -----------------------------------------
  시간초과 발생
  이중 for문을 하나로 줄여야겠다. 
  
  변경한 코드
  -----------------------------------------
  
  def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
        
    return answer
