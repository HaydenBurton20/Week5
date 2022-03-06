data = input("Enter a number or the enter button to quit: ")
number = float(data)
numbersGiven = 0
theSum = 0
while data != "":
    number = float(data)
    theSum += number
    numbersGiven += 1
    data = input("Enter a number or the enter button to quit: ")
print("The sum is", theSum)
average = theSum / numbersGiven
print("The average is", average)
