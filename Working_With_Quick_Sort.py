print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

# This code implements the quick sort algorithm


def quick_sort(array, left, right):
    if left < right:
        partition_pos = partition(array, left, right)
        quick_sort(array, left, partition_pos -1)
        quick_sort(array, partition_pos + 1, right)


def partition(array, left, right):
    i = left
    j = right
    pivot = array[right]

    while i < j:
        while i < right and array[i] < pivot:
            i += 1

        while j > left and array[j] > pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]

    return i

