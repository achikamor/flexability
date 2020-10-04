word = input("Enter a string: ")
longest = 0
str_acc = ""
current_counter = 0
for index in range(len(word)):
    if word[index] in str_acc:
        if current_counter > longest:
            longest = current_counter
        current_counter = 1
        str_acc = word[index]
    else:
        str_acc += word[index]
        current_counter += 1
if current_counter > longest:
    longest = current_counter
print(longest)
