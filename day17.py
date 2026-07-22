file_name = "data/obama_speech.txt"

with open(file_name) as f:
    lines = f.readlines()

line_count = 0
word_count = 0

for line in lines:
    line_count = line_count + 1

    in_word = False

    for ch in line:
        if ch != " " and ch != "\n" and ch != "\t":
            if in_word == False:
                word_count = word_count + 1
                in_word = True
        else:
            in_word = False

print("Number of lines:", line_count)
print("Number of words:", word_count)

#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# Your output should look like this
#print(most_spoken_languages(filename='./data/countries_data.json', 10))
#[(91, 'English'),
#(45, 'French'),
#(25, 'Arabic'),
#(24, 'Spanish'),
#(9, 'Russian'),
#(9, 'Portuguese'),
#(8, 'Dutch'),
#(7, 'German'),
#(5, 'Chinese'),
#(4, 'Swahili'),
#(4, 'Serbian')]

# Your output should look like this
#print(most_spoken_languages(filename='./data/countries_data.json', 3))
#[(91, 'English'),
#(45, 'French'),
#(25, 'Arabic')]

import json

def most_spoken_languages(filename, n):

    with open(filename, encoding="utf-8") as f:
       countries = json.load(f)

    languages = {}

    for country in countries:
        for language in country["languages"]:

            if language in languages:
                languages[language] = languages[language] + 1
            else:
                languages[language] = 1

    result = []

    while n > 0:

        maximum = 0
        language_name = ""

        for language in languages:

            if languages[language] > maximum:
                maximum = languages[language]
                language_name = language

        result.append((maximum, language_name))

        del languages[language_name]

        n = n - 1

    return result


print(most_spoken_languages("./data/countries_data.json", 10))
print(most_spoken_languages("./data/countries_data.json", 3))