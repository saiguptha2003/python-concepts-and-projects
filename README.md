<h3>code shortcuts in python</h3>

to convert a string which is a list 
like 
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
