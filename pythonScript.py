import string
import random

def stringManipulator():
    requiredString = ''

    for i in range(0,10):
        requiredString += random.choice(string.ascii_letters)

    for i in range(0,3):
        requiredString += str(random.randint(1,10))

    print(requiredString)
    reversedString = requiredString[::-1]
    print(reversedString)

    outputFile = open('output.txt', "w")  # write file to output.txt
    outputFile.write(requiredString + '\n')
    outputFile.write(reversedString + '\n')
    outputFile.close()


def main():
    stringManipulator()

#call main() which calls the single stringManipulator() function
if __name__ == '__main__':
  main()