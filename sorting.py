from inspect import indentsize


def bubblesort(array):
    for iter in range(len(array)):
        for item in range(0,len(array)-1-iter):
            if array[item] > array[item+1]:
                array[item],array[item+1] = array[item+1],array[item]

#tüm diziyi tara en küçüğü bul başa koy
def selectionsort(array):

    min_value = 10000

    for iter in range(len(array)):
        min_value = 10000
        for item in range(iter,len(array)):
            if(array[item] < min_value):
                min_value = array[item]
                index = item
        array[iter],array[index] = array[index],array[iter]
        



array = [9,1,10,6,3,15,23,4,5,4,2,7,8,6,1,33,56,889,6543,566,7,89,876,0,33,56]

selectionsort(array)

print(array)
