word = input("Enter a word: ")
origin = []
for character in word:
    origin.append(character)
reverse_list = origin[::-1]
print(reverse_list == origin)
