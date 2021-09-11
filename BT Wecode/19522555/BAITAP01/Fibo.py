def fibo(x):
  f = [0,1]
  for i in range(2,x+1):
    f.append(f[i-1] + f[i-2])
  return f[x]
#(dùng phương pháp dynamic programming)

x = int(input())
if(1<= x <=30):
  print(fibo(x))

else:
   print("So %d khong nam trong khoang [1,30]." %(x))