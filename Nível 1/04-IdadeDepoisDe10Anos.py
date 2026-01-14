#Pedir a idade do usuário
#Somar 10 à idade
#Exibir a nova idade
def lerIdade(mensagem):
    while True:      
        try:
            return int(input(mensagem))
        except ValueError:
            print('Idade é medida em números, não em letras')

idadeAtual = lerIdade('Digite a sua idade: ')
idadeFinal = idadeAtual + 10

print('Você terá',idadeFinal,'anos de idade')