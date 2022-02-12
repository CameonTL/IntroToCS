# This program calculates the number of grapevines that fit in a row based on a preset formula

# Input the information for the variables
rowLength = float(input('Enter the length of the row in feet: '))
postSpace = float(input('Enter the amount of space used by the end-post, in feet: '))
vineSpace = float(input('Enter the amount of space between grapevines, in feet: '))

# Calculate the formula with the variable rules
vinesInRow = (rowLength - (2 * postSpace)) // vineSpace

# Display the number of vines that will fit in a row
print('There can be', vinesInRow, 'vines in a row.')
