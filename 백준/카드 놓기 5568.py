from itertools import permutations

N = int(input())
K = int(input())

card = []
result = []

for i in range(N):
    card.append(input())

result = [''.join(slot) for slot in list(permutations(card,K))]
print(len(set(result)))