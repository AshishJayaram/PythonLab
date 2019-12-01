students= {"1MS17IS024":"Ani","1MS17IS026":"Anmol","1MS17IS028":"Ashay"}
list=["value1","value2","value3"]
list2=[]
j=0
for i in students:
        print("Key is ",i," Value is ",students[i])
        list[j]=students[i]
        j=j+1
print(list)
print(students.keys())
print(students.values())
print(students.items())
