#Pedir o número
#Definir se x < 0, x = 0, x > 0
# Mostrar o que ele é

#Verifica se o valor inserido é válido, se não for, repete a pergunta até o valor fornecido for 'float'
while True:
    try:
        entrada = input('Digite um número:').replace(',', '.')
        numero = float(entrada)
        break
    except ValueError:
        print('Valor inválido, digite um NÚMERO')

if(numero < 0):
    print('O número',numero,'é negativo')
elif(numero == 0):
    print('O número',numero,'é zero')
elif(numero > 0):
    print('O número',numero,'é positivo')