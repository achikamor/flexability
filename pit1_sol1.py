first = input("Enter a string: ")
second = input("Enter a string: ")
is_similar = False
if first != second:
    if sorted(first) == sorted(second):
        is_similar = True
print(is_similar)
