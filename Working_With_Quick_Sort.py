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
        print(my_nums)



print("* * * * * * * * * * * * * * * Quick Sort * * * * * * * * * * * * * * *")
my_nums = [46, 17, 16, 53, 83, 7, 13, 62, 44, 14]
print("Original Array:", my_nums, "\n")
print("Process:")
quick_sort(my_nums)
print("\nSorted Array Using QuickSort:", my_nums)