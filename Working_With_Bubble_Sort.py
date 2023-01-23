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

