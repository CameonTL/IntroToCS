# This program uses boolean statements and classes to find if an input number is prime

def prompt():
  print('Check to see if a number is prime')

# Get an input from the user
def getNum():
  inputNum = int(input('enter a number:'))
  return inputNum

# Look through the range of numbers to check if the input is prime
def primeTest(inputNum):
  count = 0
  for num in range (2, inputNum):
    numTest = inputNum % num
    if numTest == 0:
      count += 1
    if count > 0:
      return True
    else:
      return False

# Display results
def answer(prime):
  if prime:
    print('the number is not prime')
  else:
    print('the number is prime')

# Run all classes under main class
def main():
  prompt()
  inputNum = getNum()
  prime = primeTest(inputNum)
  answer(prime)

main()
