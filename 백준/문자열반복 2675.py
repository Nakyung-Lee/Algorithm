T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    new_str = []
    for j in range(len(S)):
        new_str.append(S[j]*int(R))
    print(''.join(new_str))



