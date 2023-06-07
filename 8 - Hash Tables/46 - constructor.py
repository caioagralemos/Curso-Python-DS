class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self,key):
        my_hash = 0
        for letter in key:
            # isso aqui vai retornar o endereço em que sua chave vai ficar guardada
            # é uma formula que pega os codigos ascii das letras e relaciona a um numero de 0 a size-1
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
        
my_hash_table = HashTable()
my_hash_table.print_table()