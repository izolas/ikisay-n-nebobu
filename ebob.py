def ebob(x,y):
    temp=1
    for i in range(1,min(x,y)+1):
        if (x%i==0 and y%i==0):
            x /=i
            y /=i
            temp *=i
    return temp

x=int(input("ilk sayıyı giriniz:"))
y=int(input("\nikinci sayıyı giriniz:"))
print("\n",x,"ve",y,"sayılarının EBOB'u:",ebob(x,y))
