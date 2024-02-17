class Cliente:
    def __init__(self, nome, senha, mensalidade):
        self.nome = nome
        self.senha = senha
        self.mensalidade = mensalidade

def cadastrar_cliente():
    nome = input("Digite o nome do cliente (ou 'SAIR' para encerrar): ")
    if nome.upper() == "SAIR":
        return None
    
    senha = int(input("Digite a senha de acesso (Apenas números): "))
    mensalidade = input("Situação da mensalidade (P para paga, F para devendo): ")
    
    return Cliente(nome, senha, mensalidade)

def main():
    clientes = []
    while True:
        cliente = cadastrar_cliente()
        if cliente is None or len(clientes) >= 100:
            break
        clientes.append(cliente)
    
    print("\nCadastro encerrado. Agora, informe as senhas de acesso:")
    while True:
        senha = int(input("Senha de acesso (-1 para sair): "))
        if senha == -1:
            break
        
        cliente_encontrado = None
        for cliente in clientes:
            if cliente.senha == senha:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado:
            if cliente_encontrado.mensalidade == "P":
                print(f"{cliente_encontrado.nome}, seja bem-vindo(a)!")
            else:
                print(f"Não está esquecendo de algo, {cliente_encontrado.nome}? Procure a recepção!")
        else:
            print("Seja bem-vindo(a)! Procure a recepção!")

if __name__ == "__main__":
    main()
