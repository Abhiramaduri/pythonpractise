#Conditionals

#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are old enough to drive")
else:
    x = 18-age
    print("You need",x,"more years to learn to drive")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
#Output:
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3

num1 = int(input("Enter number one"))
num2 = int(input("Enter number two"))

if (num1 > num2):
    print(num1,"is greater than",num2)
else:
    print(num2,"is greater than",num1)

# Write a code which gives grade to students according to theirs scores:
#```sh
#90-100, A
#80-89, B
#70-79, C
#60-69, D
#0-59, F
#```

score = int(input("Enter the student's score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
else:
    print("Grade: F")