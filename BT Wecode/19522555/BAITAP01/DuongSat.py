k, t = [int(x) for x in input().split()]
epx = t//k
if (epx%2==0):
  print(t-epx*k)
else:
  print((epx+1)*k - t)