# This program creates a simple table that converts tempuratures Celcius to Farenheit

# Create a header for the table
print('Celcius\tFarenheit')
print('-----------------------')

# For a set of numbers, display them and use a formula to find what they convert to
for number in range(0, 21):
  farenheit = (9 / 5) * number + 32
  print(number, '\t', format(farenheit, '.1f'))
