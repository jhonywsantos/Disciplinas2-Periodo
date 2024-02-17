def contar_buracos(texto):
    buracos = {'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1}
    total_buracos = 0
    for letra in texto:
        if letra.upper() in buracos:
            total_buracos += buracos[letra.upper()]
    return total_buracos

t = int(input("Quantos casos de teste você deseja (Selecione de 1 - 40)? "))
for _ in range(t):
    texto = input("Digite o texto: ")
    print(contar_buracos(texto))
