'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''

numeros = [0.0]*10

for i in range(10):
    numeros[i] = float(input(f'Digite o valor do número na posição {i+1}: '))
for i in range(9, -1, -1):
    print(f'O valor informado na posição {i+1} resulta em: {numeros[i]}')
