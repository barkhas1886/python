import math
a=float(input("enter first side:"))
b=float(input("enter second side:"))
c=float(input("enter third side:"))
s=(a+b+c)/2
herons_formula=(math.sqrt(s*((s-a)*(s-b)*(s-c))))
print(round(herons_formula,3))
                                  
    
