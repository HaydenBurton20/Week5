import random
import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger numver: "))
count = 0
while True:
     count += 1
     myNumber = (smaller + larger)
     print('%d %d' % (smaller, larger))
     print('Your number is %d'% myNumber)
     choice = input('Enter =,<, or >:')
     if choice == '=':
          print("Hooray, I've got it in %d tries"% count)
          break
     elif smaller == larger:
          print("I'm out of guesses, and you cheated")
          break
     elif choice == '<':
                larger = myNumber - 1
else:
        smaller = myNumber + 1
