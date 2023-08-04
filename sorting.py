"""
Insertion Sort : sorted left side, unsorted on the right
runtime best: o(n)
	worst: o(n^2)
	average: o(n^2)
storage: o(1)
use for small arrays, usually the ones that are partially sorted
 to sort in reverse order, change while statement to arr[i] < key
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


"""
Merge sort:
Divide into smaller subarrays till there are only 2 elements. Then merge it all together. Recursive - split, sort. Merge

runtime best: 
        worst:
        average: o(n log.n)

storage: o(n)

usage: large datasets, external sorting bc data too larfge to fit in memory.
can be parallelised (processors). not optimal for small data. also not in-place, is a concern do not use
inversion count prob.
"""

def merge(arr, p, q, r):
	left = arr[p:q+1]
	right = arr[q+1:r+1]
	left.append(float('inf'))
	right.append(float('inf'))

	i = 0; j = 0
	for k in range(r-r-p+1):
		if left[i] <= right[j]:
			arr[k+p] = left[i]
			i+=1
		else:
			arr[k+p] = right[j]
			j+=1
	return arr

def mergeSort(arr, p=0, r=None):
	if r == None:
		r = len(arr)-1
	if p < r:
		q = math.floor((r+p)/2)
		mergeSort(arr, p, q)
		mergeSort(arr, q+1, r)
		merge(arr, p, q, r)
	return arr


"""
heapsort
heapify, then sort

runtime average: o(n log.n)
space: o(log.n) for recursive. o(1) for iterative

typically not stable (unlike merge sort). slower than quicksort.
used for large datasets, simpler does not need recursion.
costly, unstable, not efficient for large data. 
merge takes more space, heap takes a bit more time.
uses - kth largest, priority queue, linux default 
"""
def heapify(arr, n, i):
	largest = i
	l = 2*i+1
	r = 2*i+2

	if l<n and arr[i] < arr[l]:
		largest = r

	if largest!=i:
		(arr[i], arr[largest]) = (arr[largest], arr[i])

		heapify(arr, n, largest)

def heapSort(arr):
	n = len(arr)

	for i in range(n//2-1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		heapify(arr, i, 0)

"""
quick sort

uses - all except stable sort
fastest, cache friendly, in place
kth smallet etc
primitive type methods

avg runtime = 0(n log.n)
worst case: o(n^2)

space: o(1)
"""
def partition(array, low, high):
	pivot = array[high] # rightmost is my pivot
	i = low-1

	for j in range(low,high):
		if array[j] <= pivot:
			i = i+1
			(array[i], array[j]) = (array[j], array[i])
	
	(array[i+1], array[high]) = (array[high], array[i+1])
	return i+1

def quickSort(array, low, high):
	if low<high:
		pi = partition(array, low, high)
		quickSort(array, low, pi-1)
		quickSort(array, pi+1, high)



"""
next
"""
