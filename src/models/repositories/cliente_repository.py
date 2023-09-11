from typing import List
from src.models.entities.cliente import Cliente


class ClienteRepository:
    def __init__(self) -> List:
        self.__cliente_list = []

    def cadastrar_cliente(self, nome: str, telefone: any, estado: str) -> None:
        cliente = Cliente(nome, telefone, estado)
        self.__cliente_list.append(cliente)

    def listar_clientes_por_estado(self, estado: str) -> List:
        return [cliente for cliente in self.__cliente_list if cliente.estado == estado]
