# Create a class called student , create the following attributes name , age and marks , create a method called display that prints the student destails , create two student objects 
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name, self.age, self.marks)


s1 = Student("Rahul", 19, 70)
s2 = Student("Om", 15, 90)
s1.display()
s2.display()

#write any example using single in heritance 

class Animal:
    def __init__ (self,name,age):
        self.name=name
        self.age = age

class Dog(Animal):
    def display(self):
        print(self.name,self.age)

dog1= Dog("Tommy",6)

dog1.display()




