print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

# This code implements the insertion sort algorithm


def insertion_sort(my_nums):
    for i in range(1, len(my_nums)):
        j = i
        while my_nums[j - 1] > my_nums[j] and j > 0:
            my_nums[j - 1], my_nums[j] = my_nums[j], my_nums[j - 1]
            j -= 1
            print(my_nums)


print("* * * * * * * * * * * * * * * Insertion Sort * * * * * * * * * * * * * * *")
my_nums = [46, 17, 16, 53, 83, 7, 13, 62, 44, 14]
print("Original Array:", my_nums, "\n")
print("Process:")
insertion_sort(my_nums)
print("\nSorted Array Using Insertion Sort:", my_nums)