import datetime 
def AgeConvert(num): 
    d= int(num[0] + num[1]) 
    m= int(num[3] + num[4]) 
    y= int(num[6] + num[7] + num[8] + num[9])
    print ("DoB- ",d,m,y)
    dob = datetime.datetime(y,m,d)
    new_date = datetime.datetime.today() - dob
    age = (new_date)
    print("Age= ",age)
    
num="09-02-1999" 
AgeConvert(num)
