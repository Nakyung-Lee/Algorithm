import sys

N = int(input())
# Bronze 제외 | S, G, P, D
grade = list(map(int,sys.stdin.readline().split()))
mvp_grade = list(input())

print(mvp_grade)
tot = [0]

for mvp in mvp_grade:
    if mvp == 'B':
        x = grade[0] - 1 - tot[-1]
    elif mvp == 'S':
        x = grade[1] - 1 - tot[-1]
    elif mvp == 'G':
        x = grade[2] - 1 - tot[-1]
    elif mvp == 'P':
        x = grade[3] - 1 - tot[-1]
    else:
        x = grade[3]
    tot.append(x)

print(sum(tot))