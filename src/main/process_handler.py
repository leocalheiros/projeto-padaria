from .constructors.introduction_process import introduction_process
from .constructors.cadastrar_cliente_process import cadastrar_cliente_process
from .constructors.listar_clientes_por_estado_process import listar_clientes_por_estado_process


def start() -> None:
    while True:
        command = introduction_process()

        if command =='1':
            nome = input('Digite o nome do cliente: ')
            telefone = input('Digite o telefone do cliente: ')
            estado = input('Digte o estado do cliente: ')
            cadastrar_cliente_process(nome, telefone, estado)

        elif command =='2':
            estado = input('Digite o estado para listar os clientes: ')
            listar_clientes_por_estado_process(estado)
