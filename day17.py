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
