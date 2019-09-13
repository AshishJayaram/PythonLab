def rem_dup(numbers):
    list = []
    for i in numbers:
        if i not in list:
            list.append(i)

    print (list)
    return list
def onelcomp(x):
    S=[x**2 for x in range (8)]
    print(S)
    m=[x for x in S  if x%2==0]
    m.reverse()
    print(m)

x=[1,2,3,4,5,6,3,7,2,3,7]
rem_dup(x)
onelcomp(x)