
def binary_search(arr: list[int], target: int) -> int:
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A sorted list of elements.
    target: The value to search for in the array.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (right + left) // 2

        if arr[mid] == target:
            return mid
        elif mid < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1