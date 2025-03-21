#creating a calculator using python
a= float(input("enter value 1 : "))
b= float(input("enter value 2 : "))
ope=input("Enter operation - add,sub,mul or div")
if(ope == "add"):
    print("Result=", a+b)
elif(ope== "sub"):
    print("Result=", a-b)
elif(ope== "mul"):
    print("Result=", a*b)
elif(ope== "div"):
    print("Result=", a//b)