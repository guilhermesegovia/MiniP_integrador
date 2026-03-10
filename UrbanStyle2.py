from dataclasses import dataclass
from datetime import datetime

@dataclass
class Fornecedor:
    id: int
    nome_empresa: str
    cnpj: str

@dataclass
class Produto:
    id: int
    nome: str
    categoria: str
    tamanho: str
    cor: str
    codigo_barras: str
    custo: float
    venda: float
    estoque: int
    fornecedor_id: int

@dataclass
class MovimentoEstoque:
    id: int
    produto_id: int
    tipo: str
    quantidade: int
    data_hora: str

@dataclass
class Compra:
    id: int
    produto_id: int
    quantidade: int
    total: float
    data_hora: str

@dataclass
class Cliente:
    id: int
    nome: str
    cpf: str
    email: str
    endereco: str
    data_nascimento: str
    senha: str
    numero_telefone: str

@dataclass
class Funcionario:
    id: int
    nome: str
    cpf: str
    setor: str
    cargo: str


clientes = []
fornecedores = []
movimentos = []
compras = []
produtos = []
funcionario = []
carrinho = []


def proximo_id(lista):
    return len(lista) + 1


def agora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")



# FORNECEDOR


def cadastrar_fornecedor():
    print("\n--- Cadastrar Fornecedor ---")
    nome = input("Nome da Empresa: ")
    cnpj = input("CNPJ: ")

    fornecedor = Fornecedor(
        proximo_id(fornecedores),
        nome,
        cnpj
    )

    fornecedores.append(fornecedor)
    print("Fornecedor cadastrado!")


def listar_fornecedores():
    print("\n--- Fornecedores ---")
    for f in fornecedores:
        print(f)



# PRODUTOS


def cadastrar_produto():
    if len(fornecedores) == 0:
        print("Cadastre um fornecedor primeiro.")
        return

    print("\n--- Cadastrar Produto ---")
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    tamanho = input("Tamanho: ")
    cor = input("Cor: ")
    codigo_barras = input("Código de barras: ")
    custo = float(input("Valor de custo: "))
    venda = float(input("Valor de venda: "))
    estoque = int(input("Quantidade em estoque: "))

    print("\nFORNECEDORES:")
    listar_fornecedores()
    fornecedor_id = int(input("ID do fornecedor: "))

    produto = Produto(
        proximo_id(produtos),
        nome,
        categoria,
        tamanho,
        cor,
        codigo_barras,
        custo,
        venda,
        estoque,
        fornecedor_id
    )

    produtos.append(produto)

    if estoque > 0:
        movimento = MovimentoEstoque(
            proximo_id(movimentos),
            produto.id,
            "ENTRADA",
            estoque,
            agora()
        )
        movimentos.append(movimento)

    print("Produto cadastrado!")


def listar_produtos():
    print("\n--- PRODUTOS ---")
    for p in produtos:
        print(p)



# ESTOQUE


def entrada_estoque():
    print("\n--- ENTRADA DE ESTOQUE ---")
    listar_produtos()

    pid = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))

    for p in produtos:
        if p.id == pid:
            p.estoque += quantidade

            movimento = MovimentoEstoque(
                proximo_id(movimentos),
                pid,
                "ENTRADA",
                quantidade,
                agora()
            )

            movimentos.append(movimento)

            print("Entrada registrada!")


def saida_estoque(tipo):
    print("\n--- SAÍDA DE ESTOQUE ---")
    listar_produtos()

    pid = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))

    for p in produtos:
        if p.id == pid:

            if quantidade <= p.estoque:

                p.estoque -= quantidade

                movimento = MovimentoEstoque(
                    proximo_id(movimentos),
                    pid,
                    tipo,
                    quantidade,
                    agora()
                )

                movimentos.append(movimento)

                print("Saída registrada!")

            else:
                print("Estoque insuficiente.")



# VENDAS


def comprar():
    print("\n--- COMPRA ---")
    listar_produtos()

    pid = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))

    for p in produtos:

        if p.id == pid:

            if quantidade <= p.estoque:

                p.estoque -= quantidade

                total = p.venda * quantidade

                compra = Compra(
                    proximo_id(compras),
                    pid,
                    quantidade,
                    total,
                    agora()
                )

                compras.append(compra)

                movimento = MovimentoEstoque(
                    proximo_id(movimentos),
                    pid,
                    "SAIDA_VENDA",
                    quantidade,
                    agora()
                )

                movimentos.append(movimento)

                print("Compra realizada! Total:", total)

            else:
                print("Estoque insuficiente.")



# CARRINHO


def adicionar_carrinho():

    print("\n--- Adicionar ao Carrinho ---")

    listar_produtos()

    pid = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))

    for p in produtos:

        if p.id == pid:

            if quantidade <= p.estoque:

                item = {
                    "produto_id": p.id,
                    "nome": p.nome,
                    "quantidade": quantidade,
                    "valor": p.venda
                }

                carrinho.append(item)

                print("Produto adicionado ao carrinho!")

                return

            else:
                print("Estoque insuficiente")

                return

    print("Produto não encontrado")


def ver_carrinho():

    print("\n--- Carrinho ---")

    if len(carrinho) == 0:
        print("Carrinho vazio")
        return

    total = 0

    for item in carrinho:

        subtotal = item["quantidade"] * item["valor"]

        total += subtotal

        print(f'{item["nome"]} | Qtd: {item["quantidade"]} | Subtotal: R$ {subtotal:.2f}')

    print(f"\nTOTAL: R$ {total:.2f}")



# RELATÓRIOS


def estoque_baixo():

    print("\n--- Produtos com baixo estoque ---")

    for p in produtos:

        if p.estoque < 20:

            print(f"{p.nome} está com apenas {p.estoque} unidades")


def margem_lucro():

    listar_produtos()

    pid = int(input("ID do produto: "))

    for p in produtos:

        if p.id == pid:

            lucro = p.venda - p.custo

            margem = (lucro / p.venda) * 100

            print(f"\nProduto: {p.nome}")
            print(f"Custo: {p.custo}")
            print(f"Venda: {p.venda}")
            print(f"Lucro unidade: {lucro}")
            print(f"Margem: {margem:.2f}%")

            return

    print("Produto não encontrado")



# LISTAGENS


def listar_compras():
    for c in compras:
        print(c)


def listar_movimentos():
    for m in movimentos:
        print(m)


def listar_clientes():
    for c in clientes:
        print(c)


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    numero_telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("CPF: ")

    c = Cliente(proximo_id(clientes), nome, cpf, email, endereco, data_nascimento, senha, numero_telefone)
    clientes.append(c)

    print("Cliente cadastrado com sucesso!")



# MENUS

def menu_administrativo():
    while True:
        print("\n====== MENU ADMINISTRATIVO ======")
        print("1 - Cadastrar fornecedor")
        print("2 - Cadastrar produto")
        print("3 - Cadastrar cliente")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_fornecedor()
        elif op == "2":
            cadastrar_produto()
        elif op == "3":
            cadastrar_cliente()
        elif op == "0":
            break
        else:
            print("Opção inválida")


def menu_estoque():
    while True:
        print("\n====== MENU ESTOQUE ======")
        print("1 - Entrada de estoque")
        print("2 - Saida por venda")
        print("3 - Saida por troca")
        print("4 - Saida por avaria")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            entrada_estoque()
        elif op == "2":
            saida_estoque("SAIDA_VENDA")
        elif op == "3":
            saida_estoque("SAIDA_TROCA")
        elif op == "4":
            saida_estoque("SAIDA_AVARIA")
        elif op == "0":
            break
        else:
            print("Opção inválida")


def menu_vendas():
    while True:
        print("\n====== MENU VENDAS ======")
        print("1 - Comprar produto")
        print("2 - Adicionar ao carrinho")
        print("3 - Ver carrinho")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            comprar()
        elif op == "2":
            adicionar_carrinho()
        elif op == "3":
            ver_carrinho()
        elif op == "0":
            break
        else:
            print("Opção inválida")


def menu_relatorios():
    while True:
        print("\n====== MENU RELATÓRIOS ======")
        print("1 - Listar produtos")
        print("2 - Listar compras")
        print("3 - Listar movimentos")
        print("4 - Estoque baixo")
        print("5 - Margem de lucro")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            listar_produtos()
        elif op == "2":
            listar_compras()
        elif op == "3":
            listar_movimentos()
        elif op == "4":
            estoque_baixo()
        elif op == "5":
            margem_lucro()
        elif op == "0":
            break
        else:
            print("Opção inválida")



# MENU PRINCIPAL

def menu():
    while True:
        print("\n======= URBAN STYLE =======")
        print("1 - Administrativo")
        print("2 - Estoque")
        print("3 - Vendas")
        print("4 - Relatórios")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            menu_administrativo()
        elif op == "2":
            menu_estoque()
        elif op == "3":
            menu_vendas()
        elif op == "4":
            menu_relatorios()
        elif op == "0":
            break
        else:
            print("Opção inválida")


menu()