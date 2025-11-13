# Chapter - Heap Sort

# Python program for implementation of heap Sort



def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1 # left = 2*i + 1
	r = 2 * i + 2 # right = 2*i + 2

# 	Purpose:
# To maintain the max-heap property for a given node i in an array of size n.
# 	•	largest = i → assume the current node i is the largest.
# 	•	l and r → calculate the indices of left and right children in the heap.
# 	•	Left child index = 2*i + 1
# 	•	Right child index = 2*i + 2


	if l < n and arr[i] < arr[l]:
		largest = l


	if r < n and arr[largest] < arr[r]:
		largest = r

# 		Here we check:
# 	•	If left child exists (l < n) and is greater than parent, update largest = l.
# 	•	If right child exists and is greater than current largest, update largest = r.

# This ensures that largest will store the index of the biggest value among i, l, and r.


	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i]) # swap


		heapify(arr, n, largest)
	# 	# /
	# 	If the parent is not the largest, we:
	# •	Swap the parent with the larger child.
	# •	Recursively call heapify() on the affected child index (largest) because swapping might break the heap property deeper in the tree.
	# 	# 



def heapSort(arr):
	n = len(arr)

	# We first get the length of the array.


	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

		# 	•	The elements from n//2 - 1 down to 0 are non-leaf nodes.
	# •	We call heapify() on each of them to turn the array into a max heap (where the largest element is at the root).


	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i]) # swap
		heapify(arr, i, 0)


		# 
# 		Here’s what happens:
# 	1.	The root (arr[0]) is the largest element, so we swap it with the last element (arr[i]).
# 	2.	Reduce the heap size by 1 (ignore the last element—it’s now in its correct position).
# 	3.	Call heapify() again on the reduced heap to rebuild the max-heap.

# This process continues until the entire array is sorted.



# Driver code to test above

arr = [12, 11, 13, 5, 6, 7, ]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
	print(arr[i])









