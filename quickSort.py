
def quickSort(array, reverse=False):
    if len(array) <= 1:
        return array
    
    left = []
    pivot = []
    right = []
    
    pivot_index = len(array)//2
    pivot_value = array[pivot_index]
    
    for i in range(len(array)):
        if array[i] == pivot_value:
            pivot.append(array[i])
        elif array[i] < pivot_value:
            left.append(array[i])
        else:
            right.append(array[i])
            
    if reverse:
        return quickSort(right, reverse=True) + pivot + quickSort(left, reverse=True)
    else:
        return quickSort(left) + pivot + quickSort(right)

