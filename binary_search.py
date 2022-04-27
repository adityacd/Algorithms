def binary_search(sequence, item):
    if len(sequence) > 0:
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
    else:
        print("Please enter a valid sequence")

x = [1,2,3,22,33,45,69,75,88,90,103,112,128,130,148]
#x = []
print(binary_search(x, 112)) 