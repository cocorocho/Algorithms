import random
import math


def binarySearch(arr, value):
    """
    Array needs to be sorted
    """

    if value not in arr: return None

    firstindex = 0
    lastindex = len(arr)
    middleindex = len(arr) // 2

    while True:
        if value == arr[middleindex]:
            result = middleindex                        
            return result

        elif value > arr[middleindex]:
            firstindex = middleindex
            
        elif value < arr[middleindex]:
            lastindex = middleindex

        middleindex = firstindex + (len(arr[firstindex:lastindex]) // 2)

corrects = 0

for _ in range(10000):
    array = list(set([random.randint(0,200) for _ in range(21)]))
    array = sorted(array)
    choice = array[-1]
    target = array.index(choice)
    result = binarySearch(array, choice)

    if target == result: corrects += 1

print(corrects / 10000)

    