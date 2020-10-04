word = input("Enter a word: ")
is_palindrom = True

if len(word) > 1:
    begin = 0
    end = len(word) - 1
    if len(word) % 2 == 0:
        half = int(len(word) / 2)
    else:
        half = int(len(word) / 2) + 1

    for begin in range(half):
        if word[begin] != word[end]:
            is_palindrom = False
            break
        else:
            end -= 1
print(is_palindrom)

