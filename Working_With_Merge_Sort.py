print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

# This code implements the merge sort algorithm


def merge_sort(my_nums):
    if len(my_nums) > 1:
        # Divide the array into two sub-arrays called left array and right array
        left_array = my_nums[:len(my_nums)//2]
        right_array = my_nums[len(my_nums)//2:]
