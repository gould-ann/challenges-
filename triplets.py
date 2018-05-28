# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def a_triplets(a,b):
    score = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            score[0]+=1
        elif a[i] < b[i]:
            score[1]+=1
    return score

# devins "one-liner" *ba dum tss*
def triplets_v_2(a, b):
    return [sum([1 if a[i] > b[i] else 0 for i in range(3)]), sum([1 if b[i] > a[i] else 0 for i in range(3)])]
