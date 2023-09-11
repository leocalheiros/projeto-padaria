import sys
from src.controllers.cliente_controller import ClienteController
from src.controllers.produto_controller import ProdutoController
from .constructors.introduction_process import introduction_process
from .constructors.cadastrar_cliente_process import cadastrar_cliente_process
from .constructors.listar_clientes_por_estado_process import listar_clientes_por_estado_process
from .constructors.cadastrar_produto_process import cadastrar_produto_process
from .constructors.listar_produtos_process import listar_produtos_process
from .constructors.deletar_produto_process import deletar_produto_process
from .constructors.mostrar_clientes import mostrar_clientes

cliente_controller = ClienteController()
produto_controller = ProdutoController()


def start() -> None:
    while True:
        command = introduction_process()

        if command == '1':
            nome = input('Digite o nome do cliente: ')
            telefone = input('Digite o telefone do cliente: ')
            estado = input('Digte o estado do cliente: ')
            cadastrar_cliente_process(nome, telefone, estado, cliente_controller)

        elif command == '2':
            estado = input('Digite o estado para listar os clientes: ')
            print(f"Estado a ser pesquisado: {estado}")
            listar_clientes_por_estado_process(estado, cliente_controller)

        elif command == '3':
            mostrar_clientes(cliente_controller)

        elif command == '4':
            nome = input("Digite o nome do produto: ")
            sabor = input("Digite o sabor do produto: ")
            cadastrar_produto_process(nome, sabor, produto_controller)

        elif command == '5':
            listar_produtos_process(produto_controller)

        elif command == '6':
            produto = input("Digite o produto para deletar: ")
            deletar_produto_process(produto, produto_controller)

        elif command == '7':
            sys.exit()

        else:
            print('\nComando inválido! Tente novamente!\n\n')
