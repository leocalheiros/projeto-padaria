import os


class ClienteView:
    def mostrar_clientes(self, clientes):
        self.__clear()

        if not clientes:
            print("Nenhum cliente encontrado")
            return
        print("Clientes:")
        for cliente in clientes:
            print(f"Nome: {cliente.nome} - Telefone: {cliente.telefone} - Estado: {cliente.estado}")

    def __clear(self):
        os.system('cls||clear')
