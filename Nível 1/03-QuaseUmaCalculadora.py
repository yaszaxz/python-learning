def lerNumero(mensagem):
    while True:      
        try:
            return float(input(mensagem))
        except ValueError:
            print('Valor inválido, digite apenas NÚMEROS')

print('Bem-vindo à sua quase calculadora!')

numero1 = lerNumero('Digite um número: ')
numero2 = lerNumero('Digite um segundo número: ')

soma = numero1 + numero2
diferenca = numero1 - numero2
multiplicacao = numero1 * numero2

print('Soma:', soma)
print('Diferença:', diferenca)
print('Multiplicação:', multiplicacao)

if(numero2 != 0):
    divisao = numero1 / numero2
    print('Divisão:', divisao)
else:
    print('Divisão por zero não existe')