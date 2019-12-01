def ctof():
    ctemp=int(input("Enter Temprature in degrees C-"))
    ftemp = 9.0/5.0 * ctemp + 32
    print("Temp in F- ",ftemp)
    return
def ftoc():
    ftemp=int(input("Enter Temprature in degrees F-"))
    ctemp = (ftemp - 32) * 5.0 / 9.0
    print("Temp in F- ",ctemp)
    return

def menu():
    choice = int(input("1. C to F\n2. F to C\n3. Quit\n-"))
    while choice!=3:
        if (choice==1):
            ctof()
            menu()
        elif (choice==2):
            ftoc()
            menu()
        else:
            print("Bye.")
            exit()

menu()
