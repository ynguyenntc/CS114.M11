from decimal import * 
f = float(input())
c = (f-32)*5/9
k = 273.15 + (f-32)/1.8
getcontext().prec = 6 
print(Decimal(c).normalize(),Decimal(k).normalize())