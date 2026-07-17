#Use map to create a new list by changing each country to uppercase in the countries list

countries=['usa','russia','china','india']
def change_upper(x):
    return x.upper()
result=map(change_upper,countries)
print(list(result))
