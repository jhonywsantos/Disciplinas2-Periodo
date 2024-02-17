'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor 
a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

media_alunos = []

for i in range(10):
    alunos = [float(input(f'Digite o valor da nota {j+i} do aluno {i+1}°:')) for j in range(4)]
    media = sum(alunos)/len(alunos)
    media_alunos.append(media)

media7 = len([media for media in media_alunos if media >= 7.0])
print(f'A quantidade de alunos com média acima de 7.0 é {media7}')
