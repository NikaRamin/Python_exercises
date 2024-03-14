# Write a Python program to filter a list of integers using Lambda.
myList = [1,8,6,34,556,233,988,50,31,27]
print("The original list:",myList)

even_nums = list(filter(lambda x: x%2 == 0,myList))
print("Even numbers:",even_nums)

odd_nums = list(filter(lambda x: x%2 != 0,myList))
print("Odd numbers:",odd_nums)