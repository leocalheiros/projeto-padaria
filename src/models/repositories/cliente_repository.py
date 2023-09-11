from src.models.entities.cliente import Cliente


class ClienteRepository:
    def __init__(self):
        self.__cliente_list = []

    def cadastrar_cliente(self, nome: str, telefone: any, estado: str) -> None:
        cliente = Cliente(nome, telefone, estado)
        self.__cliente_list.append(cliente)
        print("Clientes na lista:")
        for cliente in self.__cliente_list:
            print(f"Nome: {cliente.nome}, Telefone: {cliente.telefone}, Estado: {cliente.estado}")

    def mostrar_clientes(self):
        for cliente in self.__cliente_list:
            print(f"Nome: {cliente.nome}, Telefone: {cliente.telefone}, Estado: {cliente.estado}")

    def listar_clientes_por_estado(self, estado: str):
        clientes_encontrados = [cliente for cliente in self.__cliente_list if cliente.estado == estado]
        for cliente in clientes_encontrados:
            print(f"Nome: {cliente.nome}, Telefone: {cliente.telefone}, Estado: {cliente.estado}")

        return clientes_encontrados
