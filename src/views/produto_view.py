import os


class ProdutoView:
    def cadastrar_produto(self, nome: str, sabor: str) -> any:
        self.__clear()

        if not nome or not sabor:
            print("Preencha todos os campos")
            return
        print(f"Produto cadastrado com sucesso: {nome} - Sabor: {sabor}")

    def mostrar_produtos(self, produtos: any) -> any:
        self.__clear()

        if not produtos:
            print("Nenhum produto encontrado")
            return
        print("Produtos:")
        for produto in produtos:
            print(f"Nome do produto: {produto.nome} - Sabor: {produto.sabor}")

    def deletar_produto(self, produto: any) -> any:
        self.__clear()

        if not produto:
            print("Produto não encontrado")
            return
        print("Produto deletado com sucesso!")

    def __clear(self):
        os.system('cls||clear')
