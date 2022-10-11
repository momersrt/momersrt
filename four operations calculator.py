x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=input("select a transaction: (+,-,x,/):")

if z=="+" :
    print (x + y)
elif z=="-" :
    print (x - y)
elif z=="x" :
    print (x * y)
elif z=="/" :
    print (x / y)
else :
    print (".:misclick:.")
