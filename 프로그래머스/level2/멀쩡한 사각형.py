import math

def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))
  
  '''
  첫번째 풀이
  
  import math 
  def solution(w,h):
      answer=0
      n=min(w,h)
      m=max(w,h)
      l=math.ceil(m/n)
      answer=w*h-l*n

      return answer
  
  기울기를 사용해서 풀었으나 점수 - 50점 
  예외케이스 발생, 예외처리 실패 -> 다른 방법 고려
  
  '''
  
  '''
  두번째 풀이
  
  import math 
  def solution(w,h):
    answer=0
    if w>=h:
        w,h=h,w
    for i in range(1,w):
        y=(h*i//w)
        answer+=y
  
  x좌표를 고려해서 직선에 걸리지 않는 정사각형 개수 구하기 점수 - 94.4점
  한문제에 시간초과 발생,, 해결하지 못했다 -> 반복문을 사용했기에 시간 초과가 발생했다고 생각
  -> 문제를 쪼개 생각해야겠다. 반복적으로 나타나는 부분 생각
  '''
  
  '''
  최종 풀이 
  
  import math

  def solution(w,h):
      return w*h-(w+h-math.gcd(w,h))
      
  나눠지지 않는 가장 작은 수로 표현된 함수의 사각형에서 w+h-1 로 잘린부분 나타낼 수 있었다.
  반복 횟수를 어떻게 나타낼 수 있을까? -> 반복횟수의 규칙 => 최대공약수 gcd
  '''
