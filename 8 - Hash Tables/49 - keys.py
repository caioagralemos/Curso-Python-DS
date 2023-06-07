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
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for x in self.data_map[index]:
                if x[0] == key:
                    return x[1]
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

        
my_hash_table = HashTable()
my_hash_table.set_item('pig', 123)
my_hash_table.set_item('goat', 10)
my_hash_table.set_item('piggo', 1223)
my_hash_table.set_item('goatee', 101)
my_hash_table.set_item('pigglet', 1223)
my_hash_table.set_item('goateex', 1012)
my_hash_table.print_table()
print(my_hash_table.get_item('pig'))
print(my_hash_table.get_item('goateex'))
print(my_hash_table.keys())