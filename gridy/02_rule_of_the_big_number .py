from random import randint

def make_line(start, stop):
    line = ''
    for _ in range(start,stop+1):
        line += '{} '.format(randint(1,10000))
    line.rstrip(' ')
    return line

fst_line = ' '.join(list(map(str,[randint(2, 1000), randint(1, 10000), randint(1, 10000)])))
N, M, K = list(map(int, fst_line.split()))
snd_line = make_line(1,N)
nature_list = list(map(int, snd_line.split()))
nature_list.sort()
#print(len(nature_list),'::',nature_list)

''' 풀이 1
result, limit = 0, M
while limit > 0:
    if limit > K:
        result += nature_list[-1] * K
        result += nature_list[-2]
        limit = limit - K
    elif limit <= K:
        result += nature_list[-1] * K
        limit = 0
'''    
# 풀이 2
if M >= K+1:
    small_times = int(M/(K+1))
    big_times = int((K * small_times) + (M%(K+1)))
    result = (nature_list[-1] * big_times) + (nature_list[-2] * small_times)
    print(M, K)
    print(nature_list[-2], small_times)
    print(nature_list[-1], big_times)
elif M <= K:
    result = nature_list[-1] * M

print(result)