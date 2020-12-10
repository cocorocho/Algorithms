import math

def jumpSearch(arr, value):
    # Array needs to be sorted

    arr.sort()    
    stepsize = int(math.sqrt(len(arr)))
    first_index = 0
    last_index = 0
    final_index = 0
    print(stepsize)

    for _ in arr[::stepsize]:
        last_index = last_index + stepsize if last_index + stepsize != len(arr) else len(arr) - 1
        
        if value <= arr[last_index]:
            final_index = first_index

            for idx in arr[first_index:]:
                if idx == value:                    
                    print(f"Value was found at position {final_index}.")
                    return first_index
                final_index += 1
            print("Value was not found in the array.")
            return -1

                
        first_index = last_index
    

arrt = list((0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610))

jumpSearch(arrt, 610)

        
