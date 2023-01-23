print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")

# This code implements the bubble sort algorithm


def bubble_sort(my_nums):
    for i in range(len(my_nums) - 1, 0, -1):
        for j in range(i):
            if my_nums[j] > my_nums[j + 1]:
                temp = my_nums[j]
                my_nums[j] = my_nums[j + 1]
                my_nums[j + 1] = temp
                print(my_nums)


print("* * * * * * * * * * * * * * * Bubble Sort * * * * * * * * * * * * * * *")
my_nums = [46, 17, 16, 53, 83, 7, 13, 62, 44, 14]
print("Original Array:", my_nums, "\n")
print("Process:")
bubble_sort(my_nums)
print("\nSorted Array Using Bubble Sort:", my_nums)
