n=int(input('Enter month: '))
if 1<=n<=12:
    if n in (1,3,5,7,8,10,12):
        print('Month',n,'has 31 days')
    elif n in (4,6,9,11):
        print('Month',n,'has 30 days')
    elif n==2:
        print('Month',n,'has 28 or 29 days')
