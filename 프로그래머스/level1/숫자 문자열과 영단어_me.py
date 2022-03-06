def solution(s):
    answer = 0
    word=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(10):
        s=s.replace(word[i],str(i))
    return int(s)
