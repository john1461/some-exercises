def foo(n):
    list = []
    for i in range(1,n+1):
        list.append([x for x in range(1,n+1)][:i])
    return list

n = int(input('Enter a number '))
print(f'foo({n}) is {foo(n)}')