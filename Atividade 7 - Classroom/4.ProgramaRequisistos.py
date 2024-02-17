'''Faça um programa que leia um número indeterminado de valores, correspondentes a
notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não
deve ser armazenado).'''

notas = []
soma = 0

while True:
    nota = float(input('Digite o valor da sua nota, ou digite -1 pra encerrar o programa:'))
    if nota == -1:
        break
    notas.append(nota)
    soma += nota
media = soma/len(notas)

acima_da_media = len([nota for nota in notas if nota > media])
menor_7 = len([nota for nota in notas if nota < 7.0])

#a) Mostre a quantidade de valores que foram lidos;
print(f'\nQuantidade dos valores que foram lidos pelo programa: {len(notas)}')  
#b) Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(f"Os valores em sua ordem natural (que foram informados): {' '.join(map(str, notas))}")
#c) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
print("Os valores na ordem inversa à que foram informados:")
for nota in reversed(notas):
    print(nota)
#d) Calcule e mostre a soma dos valores; 
print(f'A soma dos valores foi equivalente à: {soma}')
#e) Calcule e mostre a média dos valores; 
print(f'A média dos valores foi equivalente à: {media:.2f}')
#f) Calcule e mostre a quantidade de valores acima da média calculada;
print(f'A quantidade dos valores acima da média foram: {acima_da_media}')
#g) Calcule e mostre a quantidade de valores abaixo de sete;
print(f'A quantidade dos valores cujo foram abaixo da média 7: {menor_7}')
