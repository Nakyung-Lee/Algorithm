n=int(input())

'''
1일 때 -> 1
2일 때 -> 2 (1+1) (2)
3일 때 -> 4 (1+1+1) (1+2) (2+1) (3)
4일 때 -> 7 (1+1+1+1) (1+1+2) (1+2+1) (2+1+1) (2+2) (1+3) (3+1)
5일 때 -> 11

규칙 -> f(n)=f(n-1)+f(n-2)+f(n-3) (n>3)

'''
def sums(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return sums(n-1)+sums(n-2)+sums(n-3)

for i in range(n):
    x=int(input())
    print(sums(x))
