from src.models.repositories.cliente_repository import ClienteRepository
from src.views.cliente_view import ClienteView


class ClienteController:
    def __init__(self) -> None:
        self.cliente_repository = ClienteRepository()
        self.cliente_view = ClienteView()

    def cadastrar_cliente(self, nome: str, telefone: any, estado: str) -> None:
        self.cliente_repository.cadastrar_cliente(nome, telefone, estado)
        self.cliente_view.cadastrar_cliente(nome, telefone, estado)

    def listar_clientes_por_estado(self, estado: str):
        clientes = self.cliente_repository.listar_clientes_por_estado(estado)
        self.cliente_view.mostrar_clientes(clientes)
        return clientes
