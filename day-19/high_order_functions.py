def add(n1, n2):
    return n1+n2

def calculator(n1, n2, fun):
    return fun(n1, n2)

result = calculator(2, 45, add)

print(result)