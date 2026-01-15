#Verificar se o valor recebido é válido
#Executar o loop até 0 ser digitado
#Quando receber 0, somar todos os números digitados e exibir a soma na tela
while True:
    soma = 0
    try:
        print('Digite vários números e quando quiser parar, digite 0 para exibir a soma de todos os números digitados')
        numero = int
        while int(numero != 0):
            numero = int(input('Digite um número: '))
            soma += numero
        break
    except ValueError:
        print('Valor inválido, digite um número inteiro')
print(soma)