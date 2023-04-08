strs = 'два лиса пойимали попугая'
output = ''
a = strs.split()
print(a)
for i in a:
    print(i)
    output +=i[:1]

print(output.upper())