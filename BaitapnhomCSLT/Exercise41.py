x = input('Enter the vocal range: ')
a = x[0]
b = int(x[1])
import math
if a == 'C':
  print('The interval frequency is',261.63/(pow(2,4-b)))
elif a == 'D':
    print('The interval frequency is',293.66/(pow(2,4-b)))
elif a == 'E':
    print('The interval frequency is',329.63/(pow(2,4-b)))
elif a == 'F':
    print('The interval frequency is',349.23/(pow(2,4-b)))
elif a == 'G':
    print('The interval frequency is',392.00/(pow(2,4-b)))
elif a == 'A':
    print('The interval frequency is',440.00/(pow(2,4-b)))
elif a == 'B':
    print('The interval frequency is',493.88/(pow(2,4-b)))
    