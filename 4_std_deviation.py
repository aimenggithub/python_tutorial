import math

# 1. Input
a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")

# 2. Process 
mean = (a + b + c) / 3
std_deviation = math.sqrt(((a - mean) ** 2 + (b - mean) ** 2 + (c - mean) ** 2) / 3)


# 3. Output
print("The standard deviation of the numbers is:", std_deviation)