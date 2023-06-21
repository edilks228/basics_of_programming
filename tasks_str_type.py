#№1Write a program that prints True if the letter A occurs more frequently
# in a string than the letter B, and False otherwise.

def count_A(string):
    count = 0
    for i in string:
        if i == 'A':
            count+=1
    return count
print(count_A('i cAn not be your supermAn'))

#№2 check ()

def check_brackets(string):
    brackets = 0
    for i in string:
        if i == '(':
            brackets+=1
        if i == ')':
            brackets-=1
    if brackets != 0:
        return False
    else:
        return True

print(check_brackets('i )cAn not (be your supermAn'))

#№3 count quantity of vowels letters in string

def counr_of_vowles(string):
    upper_vowles = ['A','E','I','O','U','Y']
    lower_vowles = ['a','e','i','o','u','y']
    count = 0
    for i in string:
        if i in upper_vowles or i in lower_vowles:
            count+=1
    return count

print(counr_of_vowles('hello my name is Edil'))


#№4 Double occurrence of some letter in text

def duble_occurrence(letter, string):
    if letter not in string:
        return 'this letter is not in this text'
    result = ""
    for char in string:
        if char == letter:
            result += char * 2
        else:
            result += char
    return result


print(duble_occurrence('а','мама папа'))


#№5 Given two lines. Print the letters that also appear in the and in another line.

def common_letters(string1, string2):
    out = ''
    for i in string1:
        if i in string2:
            out+=i
    return out

print(common_letters('salam aleikum', 'vaaleikum assalam'))

#№6 Given text. Print all words starting with uppercase letters of the Latin alphabet.

def find_uppercase(string):
    out = ''
    for i in string:
        if i == i.upper():
            out+=i
    return out

print(find_uppercase('Salam Aleikum'))
