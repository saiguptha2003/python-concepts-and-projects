basic_salary=int(input('enter the salary::'))

def gross_salary(basic,hpr,dpr):
    Hra=(basic*hpr)/100
    Da=(basic*dpr)/100
    gross=basic+Hra+Da
    return gross
basic=basic_salary
if basic<=10000:
        hpr=20
        dpr=80
        salary=gross_salary(basic,hpr,dpr)
        print(salary,"is the total gross amount")
elif basic<=2000:
        hpr=25
        dpr=90
        salary=gross_salary(basic,hpr,dpr)
        print(salary, "is the total gross amount")
elif basic>20000:
        hpr=30
        dpr=95
        salary=gross_salary(basic,hpr,dpr)
        print(salary, "is the total gross amount")

