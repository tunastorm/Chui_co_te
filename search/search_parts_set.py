parts = set(map(int, input().split()))
target = list(map(int, input().split()))

n = len(parts)
m = len(target)

for t in target:
    if t in parts:
        print(True, end=' ')
    else:
        print(False, end=' ')