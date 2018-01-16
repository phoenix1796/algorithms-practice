import time
"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def swap(a,b):
    return (b,a)
def quicksort(array):
    if len(array) <= 1 :
        return array
    pivot = len(array)-1
    currInd = 0
    # print("old:",array)
    # time.sleep(1)
    while pivot > currInd:
        if array[currInd]<=array[pivot] :
            currInd += 1
        else :
            temp = array[pivot-1]
            array[pivot-1] = array[pivot]
            if pivot-1 != currInd:
                array[pivot] = array[currInd]
            array[currInd] = temp
            pivot-=1
            # currInd +=1
        # print(array[currInd],":",array)        
    print("new:",array)
    if pivot == len(array)-2:
        pivot+=1
    print(array[pivot],":",array[0:pivot],":",array[pivot+1:])
    return (quicksort(array[0:pivot]) + [array[pivot]] + quicksort(array[pivot+2:])) 

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))