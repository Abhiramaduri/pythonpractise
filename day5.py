# list operations
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic_countries = countries

print(first)
print(second)
print(third)
print(scandic_countries)

# Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end

print(full_stack)