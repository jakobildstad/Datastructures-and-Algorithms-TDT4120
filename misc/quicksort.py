def main():
    array = [2,3,4,5,1,6,3,3]
    
    print(f"array: {array}")
    quicksort(array, 0, len(array) - 1)
    print(f"sorted: {array}")


def quicksort(array, left, right):
    if left < right:
        pivot = _partition(array, left, right)
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)


def _partition(array, left, right):
    """
    This is lomuto partition. 
    array[left..i-1] is "lower list"
    array[i..j-1] is "upper list"
    At the end, the pivot is put in between them.
    """
    pivot = array[right]
    i = left

    for j in range(left, right):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    
    array[i], array[right] = array[right], array[i]
    return i


if __name__ == "__main__":
    main()