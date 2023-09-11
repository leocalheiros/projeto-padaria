import os


class ClienteView:
    def cadastrar_cliente(self, nome: str, telefone: any, estado: str) -> None:
        if not nome or not telefone or not estado:
            print("Preencha todos os campos")
            return
        print(f"Cliente cadastrado com sucesso! Nome: {nome} - Telefone: {telefone} - Estado: {estado}")

    def mostrar_clientes(self, clientes):
        self.__clear()

        if not clientes:
            print("Nenhum cliente encontrado")
            return
        print("Clientes:")
        for cliente in clientes:
            print(f"Nome: {cliente.nome} - Telefone: {cliente.telefone} - Estado: {cliente.estado}")

    def listar_clientes_por_estado(self, estado: str, clientes):
        self.__clear()

        clientes_por_estado = [cliente for cliente in clientes if cliente.estado == estado]

        if not clientes_por_estado:
            print(f"Nenhum cliente encontrado no estado {estado}")
            return
        print(f"Clientes no estado {estado}:")
        for cliente in clientes_por_estado:
            print(f"Nome: {cliente.nome} - Telefone: {cliente.telefone} - Estado: {cliente.estado}")

    def __clear(self):
        os.system('cls||clear')
