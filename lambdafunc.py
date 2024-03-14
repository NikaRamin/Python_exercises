# Write a Python program to create a lambda function that adds 15 to a given number 
# passed in as an argument, 
# also create a lambda function that multiplies 
# argument x with argument y and prints the result.

sum = lambda a : a + 15
mul = lambda x,y : x * y

print("The first lambda function:",sum(7))
print("The second lambda function:",mul(4,20))
