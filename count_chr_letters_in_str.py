def count_letters(numbers, string):
    count = 0
    for i in range(len(string)):
        if string[i] == chr(numbers):
            count+=1
    return count

print(count_letters(97, 'hello my name is Edil'))
