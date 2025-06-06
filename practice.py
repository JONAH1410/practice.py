# experimenting with the variables and string operation
name = input("What's your name? ")
age = input("How old are you? ")


print("Hello " + name + " you are " + age + " years old")

# explore data types

print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'str'>

# convert age  to an integer for mathematical operation
age = int(age)
print(type(age))  # Output: <class 'int'>

# perform arithmetic operations

sum_result = age + 100
print("The sum of your age and 100 is: ", sum_result)

# play with numbers
num1 = 10
num2 = 20

print("\nSome math practice:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} ** {num2} = {num1 ** num2} (exponentiation)")
print(f"{num1} % {num2} = {num1 % num2} (modulus)")

# wrap it up


# write a program that asks the user for their name and age, and then prints out a message that says "Hello, [name]! You are [age] years old."

