'''
Crie uma função que receba dois nuymeros como parametro,
verifique e terone a quantidade(0,1 ou 2)
de numeros pares.

'''

numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe outro numero: '))

def verificar(a,b):
    if a %2 == 0 and b %2 == 0:
        print(f'Os dois números são pares')
    elif a %2 == 0 or b %2 == 0:
        if a %2 == 0:
            print(f'Somente {a} é par')
        elif b %2 == 0:
            print(f'Somente {b} é par')
    else:
        print(f'({a} e {b})Nenhum é par!')

verificar(numero1,numero2)

