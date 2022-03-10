d = [0] * 100

# 함수사용 방식  
def fibo(x):
    print(f'f({str(x)})', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(6)

# 앞서 게산된 결과를 저장하기 위한  DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수의 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])

