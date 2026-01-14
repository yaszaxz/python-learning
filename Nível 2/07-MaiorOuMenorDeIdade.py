while True:
    try:
        idade = int(input('Informe a sua idade: '))
        break
    except ValueError:
        print('Digite um número inteiro')
if(idade >= 18):
    print('Você é maior de idade e tá liberado para apostar em cassinos')
else:
    print('Você é menor de idade e infelizmente não pode apostar em cassinos')