x=int(input("birinci sayı:"))
y=int(input("ikinci sayı:"))
z=input("işlemi şeçiniz: (+,-,x,/):")

if z=="+" :
    print (x + y)
elif z=="-" :
    print (x - y)
elif z=="x" :
    print (x * y)
elif z=="/" :
    print (x / y)
elif z=="xx" :
    print (x ** y)
else :
    print (".:hatalı tuşlama yaptınız:.")