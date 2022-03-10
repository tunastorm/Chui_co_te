array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8] * 10

def quick_arrange(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right >= start and array[pivot] <= array[right]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        elif right > left:
            array[right], array[left] =  array[left], array[right]
    quick_arrange(array, start, right - 1)
    quick_arrange(array, left + 1, end)
        
quick_arrange(array, 0, len(array)-1)
print(array)