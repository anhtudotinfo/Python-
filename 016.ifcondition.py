# https://www.w3resource.com/python-exercises/python-basic-exercise-16.php

# Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference

def difference(n):
    if n <= 17 :
        return 17-n
    else :
            return (n-17) * 2

print(difference(22))
print(difference(14))