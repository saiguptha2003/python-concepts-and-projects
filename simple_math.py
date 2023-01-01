def maximum_number(l):
    maxi=l[0]
    for i in l:
        if i>maxi:
         maxi=i
    return maxi
def minimum_number(l):
    mini=l[0]
    for x in l:
        if x<mini:
            mini=x
    return mini

def product_and_addition(l):
    sum=0
    pro=1
    for i in l:
        sum=sum+i
        pro=pro*i
    print("sum:",sum)
    print("product:",pro)