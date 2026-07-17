#Use map to create a new list by changing each country to uppercase in the countries list

countries=['usa','russia','china','india']
def change_upper(x):
    return x.upper()
result=map(change_upper,countries)
print(list(result))

#Use map to create a new list by changing each number to its square in the numbers list

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda num: num ** 2, numbers))

print(squared_numbers)
