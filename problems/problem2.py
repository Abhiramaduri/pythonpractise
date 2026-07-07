#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a = 'Thirty'
b= ' Days'
c= ' Of'
d = ' Python'

print(a+b + c + d)

#Print the length of the company string using len() method and print().
c = 'company'
print(len(c))

#Change all the characters to uppercase letters using upper() method.

print(c.upper())

u= 'UPPER'
print(u.lower())

#Change "Python for Everyone" to "Python for All" using the replace method or other methods.

str = "Python for everyone"

print(str.replace('everyone' , 'all'))

#Replace the word coding in the string 'Coding For All' to Python.

chr = "Coding For All"

print(chr.replace('Coding', 'Python'))

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length= float(input("Enter length of rectangle"))
breadth = float(input("Enter breadth of rectangle"))

area= length*breadth
perimeter = (2* (length*breadth))

print(area)
print(perimeter)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120

hours = int(input("Enter no of working hours"))
rate  = float(input("Enter rate per hour"))
netearnperweek = (hours*rate)

print(netearnperweek)

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

str = 'I hope this course is not full of jargon'

print("jargon" in str)