# This program assignment required the user to input a meal cost and the program would calculate the tax, tip and new total using constants.

# Set the constants
TIP_PERCENT = 0.18
TAX_PERCENT = 0.07

# Get the cost of the meal
foodCost = int(input('Enter the total amount of the meal: $'))

# Find the tax that applies
tax = foodCost * TAX_PERCENT

foodNTax = foodCost + tax

# Find the tip that applies
tip = foodNTax * TIP_PERCENT

# Add all the values together to get the final total
totalCost = tip + foodNTax

# Display the results of the information
print('The meal cost you entered was $', format(foodCost, '.2f'), sep='')
print('The tax is $', format(tax, '.2f'), sep='')
print('The suggested tip (18%) should be $', format(tip, '.2f'), sep='')
print('The total amount due is $', format(totalCost, '.2f'), sep='')
