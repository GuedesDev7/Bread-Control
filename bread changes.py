produtos = []

def buscar_produto(nome):
    for p in produtos:
        if p["nome"].lower() == nome.lower():
            return p
    return None

def manipular_estoque(operacao):
    nome = input("Nome do produto: ").strip()
    p = buscar_produto(nome)
    
    if not p:
        print("Produto não encontrado.")
        return

    try:
        qtd = int(input(f"Quantidade para {'adicionar' if operacao == '+' else 'retirar'}: "))
        if operacao == '+':
            p["estoque"] += qtd
        elif operacao == '-':
            if qtd <= p["estoque"]:
                p["estoque"] -= qtd
            else:
                print("Erro: Estoque insuficiente.")
        print("Operação realizada!")
    except ValueError:
        print("Erro: Digite um número inteiro.")

def cadastrar_ou_editar(produto_existente=None):
    try:
        if not produto_existente:
            nome = input("Nome: ").strip()
            if buscar_produto(nome):
                print("Erro: Produto já existe.")
                return
            preco = float(input("Preço: "))
            estoque = int(input("Estoque inicial: "))
            produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
            print("Cadastrado!")
        else:
            print(f"Editando: {produto_existente['nome']}")
            novo_nome = input("Novo nome (Enter para manter): ").strip()
            novo_preco = input("Novo preço (Enter para manter): ")
            if novo_nome: produto_existente["nome"] = novo_nome
            if novo_preco: produto_existente["preco"] = float(novo_preco)
            print("Atualizado!")
    except ValueError:
        print("Erro: Dados inválidos.")

def listar_e_alertas(tipo="geral"):
    if not produtos:
        print("Estoque vazio.")
        return

    if tipo == "geral":
        print("\n--- ESTOQUE ---")
        for p in produtos:
            print(f"{p['nome']} | R${p['preco']:.2f} | Qtd: {p['estoque']}")
    elif tipo == "total":
        total = sum(p["preco"] * p["estoque"] for p in produtos)
        print(f"Patrimônio Total: R${total:.2f}")
    elif tipo == "baixo":
        baixos = [p for p in produtos if p["estoque"] < 5]
        for p in baixos: print(f"ALERTA: {p['nome']} com apenas {p['estoque']}!")

def main():
    while True:
        print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Buscar | 5-Add Estoque | 6-Remover Estoque | 7-Total | 8-Baixo | 0-Sair")
        op = input("Opção: ")

        if op == "1": cadastrar_ou_editar()
        elif op == "2": listar_e_alertas("geral")
        elif op == "3": cadastrar_ou_editar(buscar_produto(input("Nome para editar: ")))
        elif op == "4": print(buscar_produto(input("Nome para buscar: ")) or "Não encontrado")
        elif op == "5": manipular_estoque("+")
        elif op == "6": manipular_estoque("-")
        elif op == "7": listar_e_alertas("total")
        elif op == "8": listar_e_alertas("baixo")
        elif op == "0": break
        else: print("Invalido")

if __name__ == "__main__":
    main()