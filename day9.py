# def function

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a,b):
    sum=a+b
    return sum
print(add_two_numbers(10,20))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(degree):
    f=(degree*9/5)+32
    print(f)
convert_celsius_to_fahrenheit(15)  #function call
