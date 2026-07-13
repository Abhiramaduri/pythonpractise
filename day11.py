#list comprehension 


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result = [n for n in numbers if n <= 0]
print(result)

#Change the following list of lists to a list of concatenated strings:
#names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#output
#['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

result = [' '.join(name[0]) for name in names]
print(result)