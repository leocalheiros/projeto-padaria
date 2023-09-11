class ClienteView:
    def mostrar_clientes(self, clientes):
        if not clientes:
            print("Nenhum cliente encontrado")
            return
        print("Clientes:")
        for cliente in clientes:
            print(f"Nome: {cliente.nome} - Telefone: {cliente.telefone} - Estado: {cliente.estado}")
