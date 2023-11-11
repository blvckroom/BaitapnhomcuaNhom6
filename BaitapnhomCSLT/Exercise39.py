n=int(input('Sound level: '))
if n<40:
    print('Sound level has a smaller value "Quiet room"')
elif n==40:
    print('Sound level has the same value as "Quiet room"')
elif 40<=n<=70:
    print('Sound level has a value in the middle "Quiet room" and "Alarm clock"')
elif n==70:
    print('Sound level has the same value as "Alarm clock"')
elif 70<=n<=106:
    print('Sound level has a value in the middle "Alarm clock" and "Gas lawnmower"')
elif n==106:
    print('Sound level has the same value as "Gas lawnmower"') 
elif 106<=n<=130:
    print('Sound level has a value in the middle "Gas lawnmower" and "Jackhammer"') 
elif n==130:
    print('Sound level has the same value as "Jackhammer"') 
elif n>130:
    print('Sound level has a bigger value "Jackhammer"')