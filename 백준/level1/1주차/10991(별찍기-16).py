n=int(input())
print(" "*(n-1)+"*")
for i in range(2,n):
    print(" "*(n-i-1)+(" *")*i)
if n!=1:
    print("* "*n)
