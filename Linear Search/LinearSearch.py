def linearSearch(arr, value):
    for i, v in enumerate(arr):
        if v == value:
            print(f"Value was found at position {i}")
            return i
    
    print("Value was not found in given array.")
    return -1
