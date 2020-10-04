first = input("Enter a string: ")
second = input("Enter a string: ")
inputs = [first, second]
is_similar = False
if first != second and len(first) == len(second):
    first_dict = dict()
    second_dict = dict()
    dictionaries = [first_dict, second_dict]
    for current in range(len(inputs)):
        current_word = inputs[current]
        current_dict = dictionaries[current]
        for character in current_word:
            if character in current_dict:
                current_dict[character] += 1
            else:
                current_dict[character] = 1

    for dict_char_key in first_dict:
        if dict_char_key in second_dict and first_dict[dict_char_key] == second_dict[dict_char_key]:
            is_similar = True
        else:
            break

print(is_similar)
