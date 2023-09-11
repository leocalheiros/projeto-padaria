from src.controllers.cliente_controller import ClienteController


def cadastrar_cliente_process(nome, telefone, estado, cliente_controller=ClienteController):
    cliente_controller.cadastrar_cliente(nome, telefone, estado)
