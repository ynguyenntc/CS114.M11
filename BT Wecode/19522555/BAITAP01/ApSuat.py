from decimal import *
x = float(input())
k = x* 0.453592/2.54**2
getcontext().prec = 6 # lấy tối đa 6 chữ số phần nguyên và phần thập phân
print(Decimal(k).normalize())  # chuẩn hóa dữ liệu
#15	1.0546
#2018	141.879