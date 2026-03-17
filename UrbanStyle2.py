from dataclasses import dataclass
from datetime import datetime

@dataclass
class Fornecedor:
    id: int
    nome_empresa: str
    cnpj: str

@dataclass
class Cliente:
    id: int
    nome: str
    telefone: str
    cpf: str
    email: str
    senha: str
    endereco: str
    cep: str
    data_nascimento: str

@dataclass
class Funcionario:
    id: int
    nome: str
    setor: str
    cargo: str
    data_nascimento: str
    endereco: str
    cpf: str

@dataclass
class Categoria:
    id: int
    nome: str
    descricao: str

@dataclass
class Produto:
    id: int
    nome: str
    id_categoria: int
    tamanho: str
    cor: str
    codigo_barras: str
    custo: float
    venda: float
    estoque: int
    data_cadastro: str
    descricao: str
    marca: str
    id_fornecedor: int

@dataclass
class Pedido:
    id: int
    frete: float
    cupom: str
    quantidade: int
    total: float
    data_hora: str
    endereco_entrega: str
    id_cliente: int

@dataclass
class Pagamento:
    id: int
    metodo: str
    status_pagamento: str
    data_pagamento: str
    status_entrega: str
    id_pedido: int

@dataclass
class Estoque:
    id: int
    tipo: str
    quantidade: int
    data_entrada: str
    data_saida: str
    id_produto: int
    id_funcionario: int

@dataclass
class ItemPedido:
    id: int
    id_produto: int
    id_pedido: int
    quantidade: int

@dataclass
class Avaliacao:
    id: int
    comentario: str
    estrelas: float

fornecedores = []
clientes = []
funcionarios = []
categorias = []
produtos = []
pedidos = []
pagamentos = []
estoques = []
itens_pedido = []
avaliacoes = []

def proximo_id(lista):
    return len(lista) + 1

def agora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def cadastrar_fornecedor():
    nome = input("Nome da empresa: ")
    cnpj = input("CNPJ: ")
    f = Fornecedor(proximo_id(fornecedores), nome, cnpj)
    fornecedores.append(f)

def cadastrar_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    senha = input("Senha: ")
    endereco = input("Endereço: ")
    cep = input("CEP: ")
    data_nascimento = input("Data nascimento: ")
    c = Cliente(proximo_id(clientes), nome, telefone, cpf, email, senha, endereco, cep, data_nascimento)
    clientes.append(c)

def cadastrar_funcionario():
    nome = input("Nome: ")
    setor = input("Setor: ")
    cargo = input("Cargo: ")
    data_nascimento = input("Data nascimento: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    f = Funcionario(proximo_id(funcionarios), nome, setor, cargo, data_nascimento, endereco, cpf)
    funcionarios.append(f)

def cadastrar_categoria():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    c = Categoria(proximo_id(categorias), nome, descricao)
    categorias.append(c)

def cadastrar_produto():
    nome = input("Nome: ")
    id_categoria = int(input("ID categoria: "))
    tamanho = input("Tamanho: ")
    cor = input("Cor: ")
    codigo = input("Código barras: ")
    custo = float(input("Custo: "))
    venda = float(input("Venda: "))
    estoque = int(input("Estoque: "))
    descricao = input("Descrição: ")
    marca = input("Marca: ")
    id_fornecedor = int(input("ID fornecedor: "))
    p = Produto(proximo_id(produtos), nome, id_categoria, tamanho, cor, codigo, custo, venda, estoque, agora(), descricao, marca, id_fornecedor)
    produtos.append(p)

def cadastrar_pedido():
    id_cliente = int(input("ID cliente: "))
    frete = float(input("Frete: "))
    cupom = input("Cupom: ")
    quantidade = int(input("Quantidade: "))
    total = float(input("Total: "))
    endereco = input("Endereço entrega: ")
    p = Pedido(proximo_id(pedidos), frete, cupom, quantidade, total, agora(), endereco, id_cliente)
    pedidos.append(p)

def cadastrar_pagamento():
    metodo = input("Método: ")
    status_pagamento = input("Status pagamento: ")
    status_entrega = input("Status entrega: ")
    id_pedido = int(input("ID pedido: "))
    p = Pagamento(proximo_id(pagamentos), metodo, status_pagamento, agora(), status_entrega, id_pedido)
    pagamentos.append(p)

def cadastrar_estoque():
    tipo = input("Tipo: ")
    quantidade = int(input("Quantidade: "))
    id_produto = int(input("ID produto: "))
    id_funcionario = int(input("ID funcionário: "))
    e = Estoque(proximo_id(estoques), tipo, quantidade, agora(), "", id_produto, id_funcionario)
    estoques.append(e)

def cadastrar_item_pedido():
    id_produto = int(input("ID produto: "))
    id_pedido = int(input("ID pedido: "))
    quantidade = int(input("Quantidade: "))
    i = ItemPedido(proximo_id(itens_pedido), id_produto, id_pedido, quantidade)
    itens_pedido.append(i)

#Cadastro avaliação

def cadastrar_avaliacao():
    comentario = input("Comentário: ")
    estrelas = float(input("Estrelas: "))
    a = Avaliacao(proximo_id(avaliacoes), comentario, estrelas)
    avaliacoes.append(a)

# MENUS

def menu_administrativo():
    while True:
        print("\n====== MENU ADMINISTRATIVO ======")
        print("1 - Cadastrar fornecedor")
        print("2 - Cadastrar produto")
        print("3 - Cadastrar cliente")
        print("4 - Listar cliente")
        print("5 - Listar fornecedor")
        print("6 - Listar produto")
        print("7 - Cadastrar funcionário")
        print("8 - Listar funcionários")
        print("9 - Cadastrar categoria")
        print("10 - Listar categorias")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_fornecedor()
        elif op == "2":
            cadastrar_produto()
        elif op == "3":
            cadastrar_cliente()
        elif op == "4":
            listar_clientes()
        elif op == "5":
            listar_fornecedores()
        elif op == "6":
            listar_produtos()
        elif op == "7":
            cadastrar_funcionario()
        elif op == "8":
            listar_funcionarios()
        elif op == "9":
            cadastrar_categoria()
        elif op == "10":
            for c in categorias:
                print(c)
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
        print("5 - Registrar movimentação")
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
        elif op == "5":
            cadastrar_estoque()
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
        print("4 - Criar pedido")
        print("5 - Adicionar item ao pedido")
        print("6 - Registrar pagamento")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            comprar()
        elif op == "2":
            adicionar_carrinho()
        elif op == "3":
            ver_carrinho()
        elif op == "4":
            cadastrar_pedido()
        elif op == "5":
            cadastrar_item_pedido()
        elif op == "6":
            cadastrar_pagamento()
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
        print("6 - Listar pedidos")
        print("7 - Listar pagamentos")
        print("8 - Listar itens do pedido")
        print("9 - Listar avaliações")
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
        elif op == "6":
            for p in pedidos:
                print(p)
        elif op == "7":
            for p in pagamentos:
                print(p)
        elif op == "8":
            for i in itens_pedido:
                print(i)
        elif op == "9":
            for a in avaliacoes:
                print(a)
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
