from src.controllers.cliente_controller import ClienteController
from src.views.cliente_view import ClienteView


def listar_clientes_por_estado_process(estado):
    listar_clientes_view = ClienteView()
    listar_clientes_controller = ClienteController()

    clientes = listar_clientes_controller.listar_clientes_por_estado(estado)
    listar_clientes_view.listar_clientes_por_estado(estado, clientes)
