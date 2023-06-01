my_list = [11,2,31,99]

# tipos de operações com listas

# O(1)

my_list.append(7) # adding 7 no reindexing
my_list.pop() # removing last element no reindexing

# O(n)
my_list.pop(0) # removing on list (not on end) reindexing all
my_list.insert(0, 11) # adding on list (not on end) reindexing all