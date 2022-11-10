def min_sub_array(array, x):
    min_length = float('inf')

    start = 0
    end = 0
    current_sum = 0
    while end < len(array):
        current_sum += array[end]
        end += 1

        while start < end and current_sum >= x:
            current_sum -= array[start]
            start += 1
            min_length = min(min_length, end-start+1)
    return min_length

print(min_sub_array([1,2,3,4,5,7], 7)) 