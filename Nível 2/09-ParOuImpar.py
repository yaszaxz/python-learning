while True:
    try:
        numero = int(input('Digite um número: '))
        break
    except ValueError:
        print('Valor inválido, digite um número inteiro')
if(numero % 2 == 0):
    print('O número',numero,'é par')
else:
    print('O número',numero,'é ímpar')