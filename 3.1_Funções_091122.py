numero = int(input(f'Informe um numero: '))

def verificar(numero):
    if numero %2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')

verificar(numero)