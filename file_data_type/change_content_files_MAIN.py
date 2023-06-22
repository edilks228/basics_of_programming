# read contents from files
first_file = open('change_content_files#1', 'r')
content_from_first = first_file.read()
first_file.close()
second_file = open('change_content_files#2', 'r')
content_from_second = second_file.read()
second_file.close()

# change content
first_file = open('change_content_files#1', 'w')
second_file = open('change_content_files#2', 'w')
first_file.write(content_from_second)
second_file.write(content_from_first)
