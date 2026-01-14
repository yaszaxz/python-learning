#Perguntar o nome do usuário
#Digitar o nome
#Exibir a mensagem

while True:
    nome = input('Digite o seu nome: ').strip()
    nomeLimpo = nome.replace(' ', '').replace('-', '')
    
    if nomeLimpo.isalpha():
        break
    else:
        print('Nome inválido, digite apenas letras')

print('Olá,',nome)