'''given natural number. write a program to print numbers not included in decimal notation'''
def not_included_in_decimal_notation():
    num = int(input('enter the number: '))
    set_numbers = set(range(10)) # create set type content numbers 0..9

    list_num = list(map(int, str(num))) # number which were entered change from int to list
    set_num = set(list_num) #from list to set

    return set_num ^ set_numbers

# print(not_included_in_decimal_notation())


'''Resheto Eratosfen algorithm'''
def Resheto_Eratosfen(n):
    main_list = []
    for i in range(n+1):
        main_list.append(i)

    main_list[1] = 0

    i = 2
    while i<n:
        if main_list[i] != 0:
            j = i+i
            while j <= n:
                main_list[j] = 0
                j = j+i
        i+=1

    main_list = set(main_list)
    main_list.remove(0)
    return sorted(list(main_list))

# print(Resheto_Eratosfen(50))

'''given text. find the sets whose elements are those occurring in the text: '''
#1. numbers 0..9 and sign of arithmetic operations

def find_sets_numbers():
    text = input()

    digit_set = set()
    operators_set = set()

    for char in text:
        if char.isdigit():
            digit_set.add(char)
        if char in ['+','-','*','/']:
            operators_set.add(char)
    return digit_set, operators_set

#2. letters from A to F and from X to Z:
def find_sets_letters():
    text = input()

    letter_set = set()
    for char in text:
        if char.isdigit() and char in ['A', 'B', 'C', 'D', 'E', 'F'] or char in ['X', 'Y', 'Z']:
            letter_set.add(char)
    return letter_set

#3. punctuation marks and letters from E to N:
def find_stes_marks():
    text = input()

    marks_set = set()
    letter_set = set()
    for char in text:
        if char in ['.',',',':',';']:
            marks_set.add(char)
        if char in ['E','F','G','H','I','J','K','L','M','N']:
            letter_set.add(char)
    return marks_set, letter_set

'''print in alphabetical order the elements of the set composed of arbitrary letters A...Z'''
import string

def print_letters():
    letters_set = set(string.ascii_uppercase)
    sorted_letters = sorted(letters_set)
    for letters in sorted_letters:
        print(letters)

# print_letters()

'''given text. find set of lowercase latin letters included in it. 
count the number of punctuation marks and numbers in the text'''
def lowercase_letters_and_marks():
    text = input()
    all_lowercase_letters = set(string.ascii_lowercase)
    lowercase_set = set()
    marks_set = set()
    for char in text:
        if char in all_lowercase_letters:
            lowercase_set.add(char)
        if char in ['.',',',':',';']:
            marks_set.add(char)

    return lowercase_set, marks_set

# print(lowercase_letters_and_marks())

'''given text. find vowels and consonants letters '''

def find_vowels_consonants():
    text = input()
    vowels = 'AEIOUYaeiouy'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels_set = set()s
    consonants_set = set()
    for char in text:
        if char in vowels:
            vowels_set.add(char)
        if char in consonants:
            consonants_set.add(char)
    print(f'vowes letters: {vowels_set}, consonants letters: {consonants_set} ')

print(find_vowels_consonants())