from src.controllers.cliente_controller import ClienteController
from src.views.cliente_view import ClienteView


def cadastrar_cliente_process(nome, telefone, estado):
    cadastrar_cliente_views = ClienteView()
    cadastrar_cliente_controller = ClienteController()

    cadastrar_cliente_controller.cadastrar_cliente(nome, telefone, estado)
    cadastrar_cliente_views.cadastrar_cliente(nome, telefone, estado)
