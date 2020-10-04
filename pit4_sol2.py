my_list = [3, 5, 1, 6, 4, 30, 28, 23, 10, 15, 2, 9, 17, 7, 21, 8, 29, 14,
           20, 27, 12, 16, 18, 26, 11, 25, 24, 13, 19]
my_list.sort()

for i in range(1, 30):
    if my_list[i] != i+1:
        print("The missing number is: ", i+1)
        break


