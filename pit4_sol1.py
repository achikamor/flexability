total_sum = 0
for i in range(30):
    total_sum += i+1

my_list = [3, 5, 1, 6, 4, 30, 28, 23, 10, 15, 2, 9, 17, 7, 21, 8, 29, 14,
           20, 27, 12, 16, 18, 26, 11, 25, 24, 13, 19]

for number in my_list:
    total_sum -= number

print("The missing number is: ", total_sum)
