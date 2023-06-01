# O (n + n) -> O (n)
def print_its(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_its(10)