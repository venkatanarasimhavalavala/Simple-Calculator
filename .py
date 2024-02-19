print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.remainder")
a=float(input("enter the first number: "))
b=float(input("enter the second number: "))
operation=int(input("enter the option 1/2/3/4/5: "))
if operation==1:
    print("sum =",a+b)
elif operation==2:
    print("difference =",a-b)
elif operation==3:
    print("multiplication =",a*b)
elif operation==4:
    print("division =",a/b)
elif operation==5:
    print("remainder = ",a%b)
else:
    print("invalid operation,please try again")
