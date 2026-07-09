# Three numbers from user and among all those three numbers return largest number 

num1= int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))

if(num1>num2 and num1>num3):
    print("Largest number:",num1)
elif(num2>num1 and num2>num3):
    print("Largest number:",num2)
else:
    print("Largest number",num3)

dog = {
    "name":"Ben",
    'Breed':'Golden Retriever',
    'Legs': 4,
    'age' : 2
}
student = {
    'first_name':'Ravi',
    'last_name':'Tyagi',
    'gender':'male',
    'age':40,
    'marital status':'Unmarried',
    'skils':['coder','writer'],
    'country':'india',
    'city':'delhi',
    'address':
    {
        'block':9, 'phase':2 ,'vaishali_apartment':109 ,'bhajanpura':'New delhi'
    }
}
print(dog)
print(student)