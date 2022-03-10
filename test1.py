import string

def solution(sentence):
    checker = {a:0 for a in string.ascii_lowercase}
    for s in sentence.lower():
        if s.isalpha():
            checker[s] += 1
            
    result = [a for a in checker if checker[a] == 0]
    
    if len(result) == 0:
        answer = "perfect" 
    else:
        answer = ''.join(result)
    return answer