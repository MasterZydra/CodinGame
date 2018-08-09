a,b,x,y=[int(i)for i in input().split()]
while 1:
 p=""
 if y<b:y+=1;p="S"
 if y>b:y-=1;p="N"
 if x<a:x+=1;p+="E"
 if x>a:x-=1;p+="W"
 print(p)