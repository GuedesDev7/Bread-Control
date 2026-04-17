
produtos = [] #foi usado uma lista de dicionários, pois é mais adequada quando a ordem dos elementos importa. 


def buscar_produto():
    nome = input("Digite o nome do produto para buscar: ").strip()
    for p in produtos:
        if p["nome"].lower() == nome.lower(): # O lower resolve conflitos de letras maiusculas ou minusculas.
            return p
    return None 

def cadastrar_produto():
    nome = input("Digite o nome do produto: ").strip()
    try:                                                            #try/ evita que o programa quebre caso o usuário digite valores inválidos. 
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade inicial em estoque: "))
        
        produto = {"nome": nome, "preco": preco, "estoque": estoque}
        produtos.append(produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")
    except ValueError:
        print("Erro: Preço e Estoque devem ser valores numéricos.")

def listar_produtos():
    if not produtos:
        print("\nO estoque está vazio.")
        return
    print("\n--- LISTA DE PRODUTOS ---")
    for p in produtos:
        print(f"Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Estoque: {p['estoque']}")
    print("-------------------------")

def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ").strip()
    for p in produtos:
        if p["nome"].lower() == nome.lower(): # O lower resolve conflitos de letras maiusculas ou minusculas.
            produtos.remove(p)
            print(f"Produto '{nome}' removido com sucesso!")
            return
    print("Produto não encontrado.")

def editar_produto():
    p = buscar_produto()
    if p:
        print(f"Editando: {p['nome']}")
        try:                                    #O try/ evita que o programa quebre caso o usuário digite valores inválidos. 
            p["nome"] = input("Novo nome (ou Enter para manter): ") or p["nome"] #OR permite que a edição seja opcional, se nao for digitado nada o valor antigo permanece.  
            novo_preco = input("Novo preço (ou Enter para manter): ")
            if novo_preco: p["preco"] = float(novo_preco)
            print("Produto atualizado!")
        except ValueError:
            print("Erro: Valor inválido.")
    else:
        print("Produto não encontrado.")

def adicionar_estoque():
    p = buscar_produto()
    if p:
        try:      #O try/ evita que o programa quebre caso o usuário digite valores inválidos. 
            qtd = int(input(f"Quantidade para adicionar ao estoque de {p['nome']}: "))
            p["estoque"] += qtd
            print("Estoque atualizado.")
        except ValueError:
            print("Erro: Digite um número inteiro.")
    else:
        print("Produto não encontrado.")

def remover_estoque():
    p = buscar_produto()
    if p and p["estoque"] > 0:
        try: #O try/ evita que o programa quebre caso o usuário digite valores inválidos. 
            qtd = int(input(f"Quantidade para retirar: "))
            if qtd <= p["estoque"]:
                p["estoque"] -= qtd
                print("Retirada concluída.")
            else:
                print("Erro: Estoque insuficiente.")
        except ValueError:
            print("Erro: Digite um número inteiro.")
    else:
        print("Produto não encontrado ou sem estoque.")

def valor_total_estoque():
    total = sum(p["preco"] * p["estoque"] for p in produtos)
    print(f"\nValor total do patrimônio em estoque: R${total:.2f}")

def estoque_baixo():
    limite = 5
    baixos = [p for p in produtos if p["estoque"] < limite]
    if baixos:
        print("\n--- ALERTAS DE ESTOQUE BAIXO (Menos de 5 unidades) ---")
        for p in baixos:
            print(f"ALERTA: {p['nome']} tem apenas {p['estoque']} unidades!")
    else:
        print("\nNenhum produto com estoque crítico.")

# Menu Principal
while True:
    print("\n1-Cadastrar | 2-Listar | 3-Remover | 4-Editar | 5-Buscar")
    print("6-Add Estoque | 7-Remover Estoque | 8-Valor Total | 9-Estoque Baixo | 0-Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1": cadastrar_produto()
    elif opcao == "2": listar_produtos()
    elif opcao == "3": remover_produto()
    elif opcao == "4": editar_produto()
    elif opcao == "5": 
        res = buscar_produto()
        print(res if res else "Não encontrado.")
    elif opcao == "6": adicionar_estoque()
    elif opcao == "7": remover_estoque()
    elif opcao == "8": valor_total_estoque()
    elif opcao == "9": estoque_baixo()
    elif opcao == "0": break
    else: print("Opção inválida.")