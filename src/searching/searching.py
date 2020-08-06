def linear_search(arr, target):
    for i, n in enumerate(arr):
        if target == n:
            return i
        else:
            pass

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    beg_index = 0
    end_index = len(arr) - 1

    if end_index == -1:
        return -1

    while True:
        mid_index = ((end_index - beg_index) // 2) + beg_index

        if mid_index == beg_index:
            break
        elif arr[mid_index] == target:
            return mid_index
        elif arr[mid_index] > target:
            end_index = mid_index
        else:
            beg_index = mid_index

    return -1  # not found
