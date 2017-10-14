l=[]
n=int(input('number='))
print('enter',n,'numbers into list=')
i=0
while i<n:
    x=int(input())
    l.append(x)
    i=i+1
    for j in range(n+1):
        if j%2!=0:
            print(j);
    
