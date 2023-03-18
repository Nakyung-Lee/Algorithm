N = int(input())

result = []
for i in range(N):
    R, S = map(str, input().split())
    result.append([int(R),S])

for age, name in sorted(result,key = lambda x : x[0]):
    print(age, name)
