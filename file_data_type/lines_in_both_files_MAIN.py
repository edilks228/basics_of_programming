first_file = open('lines_in_both_files#1','r', encoding='utf-8')
second_file = open('lines_in_both_files#2', 'r', encoding='utf-8')

third_file = open('lines_in_both_files#3(add here).txt', 'w', encoding='utf-8')

for i in first_file:
    if i in second_file:
        third_file.write(i+'\n')

first_file.close()
second_file.close()
third_file.close()