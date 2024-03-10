# Write a Python program to find a list of integers with exactly two occurrences
# of nineteen and at least three occurrences of five.

def occurrence(numList):
    return numList.count("19") == 2 and numList.count("5") >= 3
        
        
numList = input("Enter numbers in the form of a list:\n")
print(occurrence(numList))
