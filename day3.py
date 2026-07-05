age = 21
height = 5.10
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("enter base"))
height= float(input("enter height"))
area = 0.5 *base *height
print("Area of triangle is ", area)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

a = float(input("Enter value of a"))
b = float(input("Enter value of b"))
c = float(input("Enter value of c"))
perimeter = a + b + c

print("Perimeter of triangle is : ", perimeter)

# Design a basic calculator using user input by using if else conditions by arithemetic operators 

a = float(input("Enter first value"))
b = float(input("Enter second value"))

operator= input("Enter operation")

if (operator=='+'):
    print(a+b)
elif (operator == "-"):
    print(a-b)
elif (operator == "*"):
    print(a*b)
elif (operator == "/"):
    print(a/b)
else:
    print("enter valid operation")

