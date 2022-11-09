'''
AQC_02

Escreva um algoritmo que solicite ao usuario a entrada de 5 idades e mostre na tela a classificação
da população seguindo os critérios:
média ate 18 anos - pop jovem
media entre 18 e 58 anos - pop adulta
media acima de 58 anos - população idosa

'''
# Sem lista
'''soma = 0
for i in range(5):
    idade = int(input(f"Digite a {i+1}ª idade: "))
    soma = soma + idade
media = soma/5

if media <= 18:
    print("Pop Jovem")
elif media <= 58:
    print("Pop adulta")
if media >= 58:
    print("Pop Idosa")'''

# Com listas

'''listaIdade = []
for i in range(5):
    idade = int(input(f"Digite a {i+1}ª idade: "))
    listaIdade.append(idade)

media = sum(listaIdade/len(listaIdade))
if media <= 18:
    print("Pop Jovem")
elif media <= 58:
    print("Pop adulta")
else:
    print("Pop Idosa")'''