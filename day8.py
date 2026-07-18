#loops 

#Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(0, 101):
    if i % 2 == 0:
        print(i)

for i in range(0,100):
    for j in range(i,100):
        print(i)
        print(j)