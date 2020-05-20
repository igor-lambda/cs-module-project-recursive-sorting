# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    a, b, c = 0, 0, 0
    x = len(arrA)
    y = len(arrB)
    z = x + y
    merged_arr = [0] * z

    # Starting with the first elements in each array, we compare elements in A to elements in B,
    # since A is already sorted, we know we won't find a smaller elements after the first
    while a < x and b < y:
        if arrA[a] <= arrB[b]:
            merged_arr[c] = arrA[a]
            a = a + 1
        else:
            merged_arr[c] = arrB[b]
            b = b + 1
        c = c + 1

    # Since elements are already sorted, we can append left over elements
    while a < x:
        merged_arr[c] = arrA[a]
        a = a + 1
        c = c + 1

    while b < y:
        merged_arr[c] = arrB[b]
        b = b + 1
        c = c + 1
    print("merging", merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # If len(arr) is only 1, we can just return that one to be merged
    if len(arr) > 1:
        mid = len(arr)//2
        # Before we run merge_sort on right of array, we place stackframes
        # on the call stack until len(arr) == 1.
        left = merge_sort(arr[:mid])
        # Before we get to merge left and right, we also must do he same for
        # the right branch, however we are calling the right merge_sort on right
        # of the top of the stack first.
        right = merge_sort(arr[mid:])
        # We are merging together the left most pair, then we go the parent
        # which is already split two ordered arrays, and merge those, etc.
        return merge(left, right)
    else:
        return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    if arr[mid] <= arr[start2]:  # I don't understand this
        return

    while start <= mid and start2 <= end:
        # If left is smaller or equal to right, leave it alone, incrmement left
        if arr[start] <= arr[start2]:
            start = start + 1
        else:
            value = arr[start2]
            index = start2
            # First we shift element bets left and righ to the right
            while index != start:
                arr[index] = arr[index - 1]
                index = index - 1
            # Then we assign start the value of arr[start2]
            arr[start] = value
            # Then all values get updated
            start = start + 1
            mid = mid + 1
            start2 = start2 + 1


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        mid = (l + r)//2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        merge_in_place(arr, l, mid, r)
    return arr
    
    


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
