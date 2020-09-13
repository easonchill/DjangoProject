
def Mkred(a,b,c):
    redh=open('New_red.csv',mode='w')
    count=int(a)
    
    for i in range(count):
        redh.write(b+c)
    redh.close()

