def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 가게의 부품 개수 입력
n = int(input())
# 기계에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()
m = list(map(int,input().split()))

for i in m:
    r = binary_search(array, i, 0, n-1)
    print(True if r else False, end = ' ')

