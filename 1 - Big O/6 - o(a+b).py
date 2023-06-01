# o(a+b) - apesar de serem 2 cts não é possivel definir as duas como n pois não tem o mesmo valor

def print_itemsplus(a,b):
    for i in range(a):
        print(i)
    for i in range(b):
        print(b)

# o(a*b) - a quantidade de operações é de a*b

def print_itemsmulti(a,b):
    for i in range(a):
        for j in range(b):
            print(i, j)

print_itemsplus(5,2) # 7 operações
print_itemsmulti(5,2) # 10 operações