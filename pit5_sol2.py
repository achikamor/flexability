list1 = [-741, 1, 3, 8, 9, 14, 22]
list2 = [-6, -2, 1.6, 21.4, 22, 99]

result = []
runner1, runner2 = 0, 0

while runner2+runner1 < len(list1+list2):
    if runner1 < len(list1) and runner2 < len(list2):
        if list1[runner1] < list2[runner2]:
            result.append(list1[runner1])
            runner1 += 1
        else:
            result.append(list2[runner2])
            runner2 += 1
    else:
        if runner1 < len(list1):
            result += list1[runner1:len(list1)]
        else:
            result += list2[runner2:len(list2)]
        break
print(result)