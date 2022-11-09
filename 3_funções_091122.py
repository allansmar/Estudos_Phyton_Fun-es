'''
Atv01
Escrever uma função qu3e receba um nuumero como parametro e informe se ele e positivo negativo ou zero
'''

numero = int(input(f'Informe um numero: '))

def verificar(numero):
    if numero > 0:
        print(f'{numero} é Positivo')
    elif numero < 0:
        print(f'{numero} é Negativo')
    else:
        print('Zero!')

verificar(numero)