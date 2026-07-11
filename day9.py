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

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def circle_area(r):
    pie = 3.14
    area = pie*r*r
    return area
print(circle_area(12))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(s):
    for i in s:
        print(i)
arr=['b','v','d']
print_list(arr)