file = open('tasks_txt', 'r')
count = 0
sum_nums_in_line = []
sum_even_numbers = 0
max_num = -999
for line in file:
    curr_sum = 0
    numbers = line.split()
    for letter in numbers:
        number = int(letter)
        if number > max_num:
            max_num = number
        count+=1
        curr_sum+=number
        if number % 2 == 0:
            sum_even_numbers+=number
    sum_nums_in_line.append(curr_sum)


print(sum_nums_in_line, sum_even_numbers, max_num)
