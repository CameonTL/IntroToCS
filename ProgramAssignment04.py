# This assignment calculates the amount of hotdogs and hotdog buns are needed for cookout based
# on the number of people attending, and how many hotdogs will be left in the end

# Set constants of amount per package
HOTDOGS = 10
HOTDOG_BUNS = 8

# Get information input from the user
attending = int(input('Enter the amount of people attending: '))
allowed = int(input('Enter the amount of hotdogs each person is allowed: '))

# Do some math to find how may packages of hotdogs and buns are needed
numberDogs = attending * allowed

dogPacks = numberDogs // HOTDOGS + 1
bunPacks = numberDogs // HOTDOG_BUNS + 1

# Display information found
print('You will need', format(dogPacks, ',.0f'), 'packages of hotdogs and',
      format(bunPacks, ',.0f'), 'packages of hotdog buns.')

# Find the amount of leftovers
totalDogs = dogPacks * HOTDOGS
totalBuns = bunPacks * HOTDOG_BUNS

# Display results if necessary
if totalDogs - numberDogs > 0:
  print('There will be', format(totalDogs - numberDogs, ',.0f'), 'hotdogs left.')
if totalBuns - numberDogs > 0:
  print('There will be', format(totalBuns - numberDogs, ',.0f'), 'hotdog buns left.')
