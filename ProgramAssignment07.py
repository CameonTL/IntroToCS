# This program writes input to a text file then reads it back to the user

def inputData():
  # Open text file to write into
  outfile = open('golf.txt', 'w')
  # Take user input and write it into the file, close the file and if "done" is entered
  name = input('Enter the player\'s name (or "done" to close): ')
  while name != 'done':
    score = int(input('Enter the player\'s score: '))
    # Write information on new lines into the file
    outfile.write(name + '\n')
    outfile.write(str(score) + '\n')
    name = input('Enter the player\'s name (or "done" to close): ')
  # Close the file and inform the user the task is complete
  outfile.close()
  print('Information written to golf.txt.')
  return outfile

def displayFile():
  # Open the text file to read from
  infile = open('golf.txt', 'r')
  name = infile.readline()
  # While information is read, the lines will be displayed, otherwise the file will close
  while name != '':
    name = name.rstrip()
    score = infile.readline()
    print(name, 'scored', score)
    name = infile.readline()
  # Close the file
  infile.close()
  
# Main class to run other classes
def main():
  outfile = inputData()
  displayFile()
  
# Run main()
main()
