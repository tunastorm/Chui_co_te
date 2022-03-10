from collections import deque


N, M  = 4, 5


graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]


#for i in range(N):

#    graph.append(list(map(int,input(f'input {M} numbers for line {i}: '))))
    

visited = []

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:

        return False
    

    if graph[x][y] == 0:

        graph[x][y] = 1

        dfs(x-1, y)

        dfs(x, y-1)

        dfs(x+1, y)

        dfs(x, y+1)

        return True

    return False

result = 0

for i in range(N):

    for j in range(M):

        if dfs(i,j):

            result += 1
            
print(result)