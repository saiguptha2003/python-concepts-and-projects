def hcf_calculator(number1,number2):
    if number1>number2:
        smaller=number2
    else:
        smaller=number1
    for iter in range(1,smaller+1):
        if((number1%iter==0)and (number2%iter==0)):
            hcf=iter
    return hcf
num1=54
num2=24
print("hcf==", hcf_calculator(num1,num2))

