print("quadratic equation form ::ax^2+bx+c")
a=int(input("enter the value of a="))
b=int(input("enter the value of b="))
c=int(input("enter the value of c="))
x=a
y=b
z=c
list1=[x,y,z]
print("given quadratic equation::")
print(a,"x^2+",b,"x+",c)
d=(b**2)-(4*a*c)
r1=((-b)+pow(d,0.5))/2*a
r2=((-b)-pow(d,0.5))/2*a
print(r1)
print(r2)
print(list1)
if d>0:
    print("roots are real and distint")
elif d==0:
    print("roots are real and equal")
else:
    print("roots are complex and distint")

