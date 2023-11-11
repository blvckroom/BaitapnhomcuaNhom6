a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print('Is an equilateral triangle')
    elif a==b!=c or a==c!=b or b==c!=a:
        print('Is an isosceles triangle')
    else:
        print('Is a regular triangle')