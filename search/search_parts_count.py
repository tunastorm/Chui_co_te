parts = list(map(int, input().split()))
target = list(map(int, input().split()))

n = len(parts)
m = len(target)

p_dict = dict()
for p in parts:
    if p not in p_dict:
        p_dict[p] = 1
    else:
        p_dict[p] += 1

for t in target:
    if t in p_dict:
        print(True, end=' ')
    else:
        print(False, end=' ')