def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index < end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        middle_value = sequence[midpoint]

        if item == middle_value:
            return midpoint
        
        elif item < middle_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1
    return None

x = [3,4,12,34,45,66,89,90,101,112,134,145]
print(binary_search(x, 45)) 