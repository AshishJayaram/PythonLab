def ChangeString(str):
    myStr = str
    newStr = []
    for i in myStr:
        x = chr(ord(i) + 1)
        print (x,end='')

str = "Hallelujah"
ChangeString(str)
