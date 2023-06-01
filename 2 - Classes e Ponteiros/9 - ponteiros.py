num1 = 11
num2 = num1 # a pergunta é, num2 é um link que aponta pra num1 ou num2 pega o valor de num1?

# descobrindo

print('Antes de atualizar o valor de num2:')
print('num1 =', num1)
print('num2 =', num2)

print('\nnum1 está apontando para o endereço', id(num1))
print('num2 está apontando para o endereço', id(num2))

num2 = 22 # vai cobrir o valor de 11 ou vai fazer a variavel apontar pra outro lugar?
print('\nDepois de atualizar o valor de num2:')
print('num1 =', num1)
print('num2 =', num2)

print('\nnum1 está apontando para o endereço', id(num1))
print('num2 está apontando para o endereço', id(num2)) # faz a variável apontar pra outro lugar