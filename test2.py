def solution(arr):
    answer = dict()
    memo = [0] * 100001
    
    for n in arr:
        if n not in answer and memo[n+1] == 0:
            answer[n] = 1
        else: 
            if memo[n+1] == 0:
                answer.pop(n)
                memo[n+1] += 1

    answer = list(answer.keys())       
    if answer == []:
        answer.append(-1)
    
    return sorted(answer)

arrs = [   
    [2, 1, 3, 3],
    [3, 4, 4, 2, 5, 2, 5, 5],
    [3, 5, 3, 5, 7, 5, 7]
] 

for arr in arrs:
    print(solution(arr))