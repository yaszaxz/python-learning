def verificarNota(mensagem):
    while True:
        try:
            entrada = input(mensagem).replace(',', '.')
            nota = float(entrada)
            if not(0 <= nota <= 10):
                print('A nota deve ser um valor de 0 a 10')
                continue
            if('.') in entrada:
                casasDecimais = len(entrada.split('.')[1])
                if casasDecimais > 2:
                    print('Máximo de duas casas decimais')
                    continue
            
            return nota
        except ValueError:
            print('Notas são valores numéricos')

nota1 = verificarNota('Nota 1: ')
nota2 = verificarNota('Nota 2: ')
nota3 = verificarNota('Nota 3: ')
nota4 = verificarNota('Nota 4: ')

media = (nota1 + nota2 + nota3 + nota4)/4
print('Média:', round(media, 2))
if(media >= 7):
    print('Aprovado(a)')
elif(5 <= media < 7):
    print('Estás recuperação')
elif(media < 5):
    print('Reprovado(a)')