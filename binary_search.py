
from colorsys import rgb_to_hls
import math
from turtle import right

#recursion
def binary_search_rescursion(array,target):
    
    left = 0
    right = len(array) - 1

    result = helper(array,left,right,target)
    return result

def helper(array,left,right,target):

    if(left > right):
        return -1

    middle = (left + right) // 2

    if array[middle] == target:
        return middle
    
    if array[middle] < target:
        left = middle + 1
    else:
        right = middle - 1
        
    return helper(array,left,right,target)

#iteration
def binary_search(array,target):

    left = 0
    right = len(array)
    middle = (left + right) // 2

    iteration = int(math.log(len(array),2))
    
    for i in range(iteration):

        if target == array[middle]:
            return middle
        
        elif target < array[middle]:
            left = 0
            right = middle - 1

        else:
            left = middle + 1
            right = len(array) - 1
        
        middle = (left + right) // 2

search_array = [1,5,7,11,54,100,250,300]

print(binary_search_rescursion(search_array,12))
