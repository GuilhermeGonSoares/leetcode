def sum_sub_array_k(array, k):
    current_sum = sum(array[:k])
    sums = [current_sum]
    for i in range(1, len(array)-k+1):
        current_sum -= array[i-1]
        current_sum += array[i+k-1]
        sums.append(current_sum)
    return sums


print(sum_sub_array_k([1,2,3,4,5,6], 5))