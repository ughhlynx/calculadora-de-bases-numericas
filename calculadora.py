
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
 [1] converter para número BINÁRIO
 [2] converter para número OCTAL
 [3] converter para HEXADECIMAL''')
alt = int(input('Sua opção: '))

if alt == 1:
    binary = bin(num)
    print('{} convertido para BINÁRIO é igual a {}.' .format(num, binary[2:]))
elif alt == 2:
    octal = oct(num)
    print('{} convetido para OCTAL é {}.' .format(num, octal[2:]))
elif alt == 3:
    hexadecimal = hex(num)
    print('{} convertido para HEXADECIMAL é {}.' .format(num, hexadecimal[2:]))
else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')
