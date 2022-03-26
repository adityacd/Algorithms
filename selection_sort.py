def selection_sort(sequence):
    initial_index = range(0, len(sequence)-1)
    

    for i in initial_index:
        min_value = i
        for j in range(i+1, len(sequence)):
            if sequence[j] < sequence[min_value]:
                min_value = j
            
        if min_value != i:
            sequence[min_value], sequence[i] = sequence[i], sequence[min_value]

    return sequence


x = [2,4,1,5,8,22,0,3]
print(selection_sort(x))
