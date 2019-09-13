def rem_dup(numbers):
    list = []
    for i in numbers:
        if i not in list:
            list.append(i)

    print (list)
    return list
rem_dup([1,2,3,4,5,6,3,7,2,3,7])