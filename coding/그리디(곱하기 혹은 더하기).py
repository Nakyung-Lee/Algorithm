N=input()

sum=0

s=[]
for i in range(len(N)):
    s.append(N[i])
    if int(N[i])==0 or int(N[i])==1:
        s.append('+')
    else:
        s.append('X')

for i in range(1,len(s)-1):
    if s[i]=='+':
        sum+=(sum+int(s[i+1]))
    elif s[i]=='X':
        sum=(sum*int(s[i+1]))

print(sum)
        
------------------------------------------------------------------------------------------

data=input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우 곱하기보다는 더하기 수행
  num=int(data[i])
  # 결과값에 추가해서 더하거나 곱하는 행위
  if num<=1 or result <=1:
    result += num
  else:
    result *= num
    
print(result)
   



