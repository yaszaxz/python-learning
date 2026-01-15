#Pedir o número para calcular a tabuada
#Criar a repetição com for para calcular a tabuada automaticamente
#(Multiplicar o número recebido pela variável i)
while True:
    try:
        numero = int(input('Digite um número e descubra a sua tabuada: '))
        for i in range(1, 11):
            tabuada = numero * i
            print(tabuada)
        break
    except ValueError:
        print('Valor inválido, digite um número')