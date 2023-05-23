<h3>code shortcuts in python</h3>

<h4>1.Code to convert String list into list to convert a string which is a list </h4>

```python
s="['1','2','3','4','5']"
```
to a list with integer items 
code :

```python bold
s="['1','2','3','4','5']"
ds=eval(s)
print(ds)
num=[]
for i in ds:
    num.append(eval(i))
for i in num:
    print(type(i))
print(num)
```
<h4>2.Code to get the largest string in the given sentence</h4> 

code:
```python
str="Gener fd re dff ereefdf"
s=str.split(" ")
f=""
for i in s:
    if(len(f)<len(i)):
        f=i
        print(i)
print(len(f))
```
<h4>3.Code to input numbers in strings in list in one sentence</h4>

```python
l=[]
l=[int(item) for item in input().split()]
print(l)
```

<h4>4.Code to reverse string using function</h4>

```python
def reverse(s):
    return s==s[::-1]
print(reverse)
```
<h4>5.Code to use lambda functions</h4>

```python
cude=lambda x:x**3
print(cude(3))
```
<h4>6.Code to get factorial in easy way</h4>

```python
def factorial(s):
    fac=1
    for i in range(1,s+1):
        fac=fac*i
    return fac
print(factorial(5))
```
<h4>7.Code to fibonacci series in easy way</h4>

```python
def fibonacci(s):
    if(s<=1):
        return s
    else:
        return fibonacci(s-1)+fibonacci(s-2)
print(fibonacci(9))
```

<h4>8.Code to lcm of two numbers</h4>

```python
def lcm(x,y):
    if(x>y):
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0 and greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
```
<h4>9.Code to reverse a string using reversed function</h4>

```python
str=""
for i in reversed("pandusai"):
    str=str+i
print(str)
```

<h4>10.Useful Methods to perform maths functions</h4>

```python
import math as m
print(m.factorial(5))
print(m.gcd(4,6))
print(m.sqrt(9))
print(m.isqrt(4))
print(m.lcm(4,6))
print(m.pow(4,2))
l=[1,2,3,4,5,6,7,8,9]
print(m.fsum(l))
print(m.prod(l))
```

