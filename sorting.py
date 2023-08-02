"""
Insertion Sort : sorted left side, unsorted on the right
runtime best: 
	worst:
	average:
storage:
"""

def insertion_sort(in_array:list) -> list:
    for (idx, key) in enumerate(in_array[1:]):
        i = idx # key = a[i+1]
        while i > -1 and in_array[i] > key:
            in_array[i+1] = in_array[i]
            i = i-1
        in_array[i+1] = key
    return in_array

in_array = [1,5,6,2,8,0]
assert insertion_sort(in_array) == [0,1,2,5,6,8]
#print(insertion_sort(in_array))
