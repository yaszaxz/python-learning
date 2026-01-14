#Receber os números
#Verificar qual é o maior
#Mostrar qual é o maior
def verificacao(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digite um número inteiro')
numero1 = verificacao('Digite um número: ')
numero2 = verificacao('Digite um segundo número: ')
numero3 = verificacao('Digite um terceiro número: ')

if(numero2 < numero1 >numero3):
    print('O maior número dentre os dados é o número', numero1)
elif(numero1 < numero2 >numero3):
    print('O maior número dentre os dados é o número', numero2)
elif(numero1 < numero3 >numero2):
    print('O maior número dentre os dados é o número', numero3)    