import sys
from .constructors.introduction_process import introduction_process
from .constructors.cadastrar_cliente_process import cadastrar_cliente_process
from .constructors.listar_clientes_por_estado_process import listar_clientes_por_estado_process
from .constructors.cadastrar_produto_process import cadastrar_produto_process
from .constructors.listar_produtos_process import listar_produtos_process
from .constructors.deletar_produto_process import deletar_produto_process
from .constructors.cadastrar_loja_process import cadastrar_loja_process
from .constructors.listar_lojas import listar_lojas_process
from .constructors.deletar_loja_process import deletar_loja_process


def start() -> None:
    while True:
        command = introduction_process()

        if command == '1':
            nome = input('Digite o nome do cliente: ')
            telefone = input('Digite o telefone do cliente: ')
            estado = input('Digte o estado do cliente: ')
            cadastrar_cliente_process(nome, telefone, estado)

        elif command == '2':
            estado = input('Digite o estado para listar os clientes: ')
            listar_clientes_por_estado_process(estado)

        elif command == '3':
            nome = input("Digite o nome do produto: ")
            sabor = input("Digite o sabor do produto: ")
            loja = input("Digite o nome da loja do produto: ")
            cadastrar_produto_process(nome, sabor, loja)

        elif command == '4':
            listar_produtos_process()

        elif command == '5':
            produto = input("Digite o produto para deletar: ")
            deletar_produto_process(produto)

        elif command == '6':
            nome = input("Digite o nome da loja: ")
            cadastrar_loja_process(nome)

        elif command == '7':
            listar_lojas_process()

        elif command == '8':
            nome = input("Digite o nome da loja para deletar: ")
            deletar_loja_process(nome)

        elif command == '9':
            sys.exit()

        else:
            print('\nComando inválido! Tente novamente!\n\n')
