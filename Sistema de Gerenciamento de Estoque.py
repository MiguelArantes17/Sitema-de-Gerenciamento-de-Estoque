
estoque = {}

def adicionar_produto(codigo, nome, quantidade, preco):
    if codigo in estoque:
        print(" Código já cadastrado.")
    else:
        estoque[codigo] = {"nome": nome, "quantidade": quantidade, "preco": preco}
        print(f" Produto {nome} adicionado com sucesso!")

def remover_produto(codigo):
    if codigo in estoque:
        removido = estoque.pop(codigo)
        print(f" Produto {removido['nome']} removido com sucesso!")
    else:
        print(" Produto não encontrado.")

def atualizar_produto(codigo, quantidade=None, preco=None):
    if codigo in estoque:
        if quantidade is not None:
            estoque[codigo]["quantidade"] = quantidade
        if preco is not None:
            estoque[codigo]["preco"] = preco
        print(" Produto atualizado com sucesso!")
    else:
        print(" Produto não encontrado.")

def buscar_produto(codigo):
    if codigo in estoque:
        produto = estoque[codigo]
        print(f" Código: {codigo} | Nome: {produto['nome']} | "
              f"Qtd: {produto['quantidade']} | Preço: R${produto['preco']:.2f}")
    else:
        print(" Produto não encontrado.")

def listar_produtos():
    if estoque:
        print("\n Lista de produtos em estoque:")
        for codigo, produto in estoque.items():
            print(f"Código: {codigo} | Nome: {produto['nome']} | "
                  f"Qtd: {produto['quantidade']} | Preço: R${produto['preco']:.2f}")
    else:
        print(" Nenhum produto cadastrado.")

def relatorio():
    if estoque:
        total = sum(p["quantidade"] * p["preco"] for p in estoque.values())
        baixo_estoque = [p["nome"] for p in estoque.values() if p["quantidade"] < 5]
        print(f"\n Valor total em estoque: R${total:.2f}")
        if baixo_estoque:
            print(" Produtos com baixo estoque:", ", ".join(baixo_estoque))
    else:
        print(" Estoque vazio.")

# Menu principal
def menu():
    while True:
        print("\n=== SISTEMA DE ESTOQUE ===")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar produto")
        print("4. Buscar produto")
        print("5. Listar produtos")
        print("6. Relatório")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código: ")
            nome = input("Nome: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            adicionar_produto(codigo, nome, quantidade, preco)

        elif opcao == "2":
            codigo = input("Código do produto: ")
            remover_produto(codigo)

        elif opcao == "3":
            codigo = input("Código do produto: ")
            quantidade = input("Nova quantidade (ou Enter para manter): ")
            preco = input("Novo preço (ou Enter para manter): ")
            atualizar_produto(
                codigo,
                int(quantidade) if quantidade else None,
                float(preco) if preco else None
            )

        elif opcao == "4":
            codigo = input("Código do produto: ")
            buscar_produto(codigo)

        elif opcao == "5":
            listar_produtos()

        elif opcao == "6":
            relatorio()

        elif opcao == "0":
            print(" Saindo do sistema...")
            break

        else:
            print(" Opção inválida.")

# Executar o sistema
if __name__ == "__main__":
    menu()
