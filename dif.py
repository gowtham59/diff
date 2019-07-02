m1,j2=map(str,input().split())

a3=0

if len(m1)>len(j2):

  m1,j2=j2,m1

i=0

while i<len(m1):

  a3+=(ord(j2[i])-ord(m1[i]))

  i+=1

for i in range(i,len(j2)):

  a3+=ord(j2[i])-ord('a')+1

print(a3)
