dict1 = {
    'value': 11
}

dict2 = dict1

print('Antes de atualizar o valor de dict2:')
print(f'\ndict1 ({dict1}) está apontando para o endereço', id(dict1))
print(f'dict2 ({dict2}) está apontando para o endereço', id(dict2)) 

dict2['value'] = 22

print('\nDepois de atualizar o valor de dict2:') 
# alterar o valor de dict2['value'] altera os valores dos dois dicts
print(f'\ndict1 ({dict1}) está apontando para o endereço', id(dict1))
print(f'dict2 ({dict2}) está apontando para o endereço', id(dict2)) 