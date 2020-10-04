word = input("Enter a string: ")
longest = 0
current_counter = 0
char_dict = dict()
running = 0

for character in word:
    if character in char_dict and char_dict[character] == running:
        running += 1
        char_dict[character] = running
        if current_counter > longest:
            longest = current_counter
        current_counter = 1

    else:
        char_dict[character] = running
        current_counter += 1

if current_counter > longest:
    longest = current_counter
print(longest)