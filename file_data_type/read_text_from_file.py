text = open('read_text', 'r',encoding='utf-8')
# read lines:
for line in text:
    print(line, end='')

# read letters:
for line in text:
    for letter in line:
        print(letter)

text.close()