n=10#int(input())
l=[['*']*n for x in range(n)]

for i in range(n):
    
    for j in range(i,len(l)):
        #print(i,j,n-j)
        
        l[n-1-i][j]=str(j-i+1 if j-i+1<3 else 2)
        #l[n-1-(j-i)][nj]=str(i)
for x in l:
    print(' '.join(x))
