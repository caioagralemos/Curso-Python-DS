def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1): 
        # começa em len(my_list) -1 e vai diminuindo até chegar a 0
        # isso é tipo um contador que começa na len da lista - 1  que vai diminuindo um por iteração
        # que é a quantidade de operações a serem realizadas por iteração
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j] 
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(bubble_sort([4,2,6,5,1,3]))