#!/usr/bin/env python3

def admin_login(username, password):
    if (username =="admin" or username =='ADMIN') and password=='12345':
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    if temperature <40:
        return "It's brisk out there!"
    elif temperature >=40 and temperature <65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return  "It's perfect out there!"
    pass

def fizzbuzz(num):
    three_multiple = num % 3 == 0
    multiple_of_five = num % 5 ==0
    if three_multiple and multiple_of_five:
        return "FizzBuzz"
    if three_multiple:
        return 'Fizz'
    elif multiple_of_five:
        return 'Buzz'
    else:
        return num
    # your code here
    pass

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        print("Invalid operation!")
        return None                  
