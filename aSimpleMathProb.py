# Write a Python program that accepts an integer (n) 
# and computes the value of n+nn+nnn

n = int(input("Enter the number:\n"))
n2 = n*n
n3 = n2*n
print("The value of n+nn+nnn is:",n+n2+n3)