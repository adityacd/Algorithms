def insertion_sort(sequence):
    initial_index = range(1, len(sequence))

    for i in initial_index:
        values_to_sort = sequence[i]

        while sequence[i-1] > values_to_sort and i>0:
            sequence[i-1], sequence[i] = sequence[i], sequence[i-1]
            i = i-1
    return sequence

x = [2,4,1,5,8,22,0,3, -2, 3434,-34]
print(insertion_sort(x))