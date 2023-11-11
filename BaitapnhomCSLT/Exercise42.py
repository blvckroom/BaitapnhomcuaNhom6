n=float(input('Frequency value: '))
if n==261.63:
    print('The musical range corresponds to the note C4')
elif n==293.66:
    print('The musical range corresponds to the note D4')
elif n==329.63:
    print('The musical range corresponds to the note E4')
elif n==349.23:
    print('The musical range corresponds to the note F4')
elif n==392.00:
    print('The musical range corresponds to the note G4') 
elif n==440.00:
    print('The musical range corresponds to the note A4') 
elif n==493.88:
    print('The musical range corresponds to the note B4') 
else:
    print('Frequency does not correspond to a known note')