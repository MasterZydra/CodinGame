n=input()
s=input().split(' ')
l=5526
try:
 for m in s:
  m=float(m)
  if abs(m)<abs(l)or abs(m)==abs(l)and m>l:l=int(m)
 print(l)
except:print(0)