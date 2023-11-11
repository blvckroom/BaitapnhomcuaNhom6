n=str(input('Enter a letter: '))
if n in ('a','e','i','o','u'):
    print('The entered letter is a vowel.')
elif n == 'y':
    print('The letter y can be a vowel or a consonant.')
else:
    print('Entered letters are consonants')