from fractions import Fraction
print("of the series")
N=int(input("enter the N :"))
sum=0

for x in range(1,N+1):
    number=1/(x)
    print(round(number,3))
    sum=sum+number
print(round(sum,4))
#fraction canbe used here to see in fraction form 
