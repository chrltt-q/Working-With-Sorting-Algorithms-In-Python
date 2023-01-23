print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

# This code implements the quick sort algorithm


def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()

    greater_elements = []
    lesser_elements = []

    for item in array:
        if item > pivot:
            greater_elements.append(item)
        else:
            lesser_elements.append(item)

    print(quick_sort(lesser_elements) + [pivot] + quick_sort(greater_elements))
    return quick_sort(lesser_elements) + [pivot] + quick_sort(greater_elements)


print("* * * * * * * * * * * * * * * Quick Sort * * * * * * * * * * * * * * *")
my_nums = [46, 17, 16, 53, 83, 7, 13, 62, 44, 14]
print("Original Array:", my_nums, "\n")
print("Process:")
print("\nSorted Array Using QuickSort:", quick_sort(my_nums))