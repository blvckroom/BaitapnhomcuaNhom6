n=int(input("Day: "))
t=int(input("Month: "))
if n==1 and t==1:
    print("New year's day")
elif n==1 and t==7:
    print("Canada day")
elif n==25 and t==12:
    print("Christmas day")
else:
    print("Not correspond to a fixed holiday")