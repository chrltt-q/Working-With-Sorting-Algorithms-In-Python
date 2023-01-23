print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

# This code implements the merge sort algorithm


def merge_sort(array):
    if len(array) > 1:
        # Divide the array into two sub-arrays called left array and right array
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        # Merge the left array and right array
        i = 0  # for the index of left array
        j = 0  # for the index of right array
        k = 0  # for merged index of left and right arrays
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

        print("Left Array:", left_array)
        print("Right Array:", right_array)


print("* * * * * * * * * * * * * * * Merge Sort * * * * * * * * * * * * * * *")
my_nums = [46, 17, 16, 53, 83, 7, 13, 62, 44, 14]
print("Original Array:", my_nums, "\n")
print("Process:")
merge_sort(my_nums)
print("\nSorted Array Using Merge Sort:", my_nums)