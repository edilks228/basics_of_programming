import random
# 1. create numbers that -100 < numbers < 100
def create_numbers(min,max,count,file):
    text = open(file, 'w')
    for i in range(count):
        number = random.randint(min,max)
        text.write(str(number)+ ' ')
    text.close()

create_numbers(-100,100,50,'count_equal_numbers_txt')
def count_numbers(file):
    file = open(file,'r')
    number_counts = {}
    for line in file:
        numbers = line.split()

        for number in numbers:
            number = int(number)

            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1
    file.close()
    return number_counts

out = count_numbers('count_equal_numbers_txt')


for number, count in out.items():
    print(f"Число {number} встречается {count} раз(а) в файле.")