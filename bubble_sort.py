def bubble_sort(sequence):
    initial_index = len(sequence) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, initial_index):
            if sequence[i] > sequence[i+1]:
                sorted = False
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]

    return sequence

x = [2,4,1,5,8,22,0,3]
print(bubble_sort(x))