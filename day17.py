#Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
#Read obama_speech.txt file and count number of lines and words

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

#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# Your output should look like this
#print(most_populated_countries(filename='./data/countries_data.json', 10))

#[
#{'country': 'China', 'population': 1377422166},
#{'country': 'India', 'population': 1295210000},
#{'country': 'United States of America', 'population': 323947000},
#{'country': 'Indonesia', 'population': 258705000},
#{'country': 'Brazil', 'population': 206135893},
#{'country': 'Pakistan', 'population': 194125062},
#{'country': 'Nigeria', 'population': 186988000},
#{'country': 'Bangladesh', 'population': 161006790},
#{'country': 'Russian Federation', 'population': 146599183},
#{'country': 'Japan', 'population': 126960000}
#]

# Your output should look like this

#print(most_populated_countries(filename='./data/countries_data.json', 3))
#[
#{'country': 'China', 'population': 1377422166},
#{'country': 'India', 'population': 1295210000},
#{'country': 'United States of America', 'population': 323947000}
#]

#Extract all incoming email addresses as a list from the email_exchange_big.txt file.

#Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
    # Your output should look like this
    #print(find_most_common_words('sample.txt', 10))
    #[(10, 'the'),
    #(8, 'be'),
    #(6, 'to'),
    #(6, 'of'),
    #(5, 'and'),
    #(4, 'a'),
    #(4, 'in'),
    #(3, 'that'),
    #(2, 'have'),
    #(2, 'I')]

    # Your output should look like this
    #print(find_most_common_words('sample.txt', 5))

    #[(10, 'the'),
    #(8, 'be'),
    #(6, 'to'),
    #(6, 'of'),
    #(5, 'and')]