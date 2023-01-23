print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")


def selection_sort(my_nums):

    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if my_nums[j] < my_nums[minpos]:
                minpos = j

        temp = my_nums[i]
        my_nums[i] = my_nums[minpos]
        my_nums[minpos] = temp
