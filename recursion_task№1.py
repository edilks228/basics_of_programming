arr = [0,10,20,30]
i = int(input(': '))
out = []
def fn(ar,i):
    if ar == []:
        return 0
    elif ar[0] > i:
        out.append(ar[0])
        return fn(ar[1:],i)
    else:
        return fn(ar[1:],i)




fn(arr,i)
print(out)

