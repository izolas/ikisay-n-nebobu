def ebob(x,y):
    temp=1
    for i in range(1,min(x,y)+1):
        if (x%i==0 and y%i==0):
            x /=i
            y /=i
            temp *=i
    return temp

def ekok(x,y):
    temp2=1
    for i in range(1,min(x,y)+1):
        if (x%i==0 and y%i==0):
            x /=i
            y /=i
            temp2 *=i
    return temp2*x*y

#ekok(x,y)=x*y/ebob(x*y)

x=int(input("ilk sayıyı giriniz:"))
y=int(input("\nikinci sayıyı giriniz:"))
print("\n",x,"ve",y,"sayılarının EBOB'u:",ebob(x,y))
print("\n {} ve {} sayılarının EKOK'u: {:.0f}".format(x,y,ekok(x,y)))
