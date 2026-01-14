#Pedir o número
#Fazer as operações
#Exibir na tela
def lerNumero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um NÚMERO!')

numero = lerNumero('Digite um número: ')

dobro = numero * 2
triplo = numero * 3
quadrado = numero ** 2
raiz = numero ** 0.5 #Não tem um símbolo que represente raiz quadrada, então tem que elevar a meio

print('Dobro:', dobro)
print('Triplo:', triplo)
print('Quadrado:', quadrado)
if(numero >= 0):
    print('Raiz quadrada:', raiz)
else:
    print('Esse número não possui raiz quadrada.')