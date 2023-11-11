n=int(input('Number year: '))
if 0<=n<=2:
    print('Dog age is ',n*5.25,' year.',sep='')
elif n>2:
    print('Dog age is ',10.5+(n-2)*4,' year.',sep='')
else:
    print('Error!!')