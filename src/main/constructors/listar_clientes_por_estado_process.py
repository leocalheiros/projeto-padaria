from src.controllers.cliente_controller import ClienteController


def listar_clientes_por_estado_process(estado, cliente_controller: ClienteController):
    cliente_controller.listar_clientes_por_estado(estado)
