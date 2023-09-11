class ProdutoView:
    def cadastrar_produto(self, nome: str, sabor: str, loja: str) -> any:
        if not nome or not sabor or not loja:
            print("Preencha todos os campos")
            return
        print(f"Produto cadastrado com sucesso: {nome} - Sabor: {sabor} - Loja: {loja}")

    def mostrar_produtos(self, produtos: any) -> any:
        if not produtos:
            print("Nenhum produto encontrado")
            return
        print("Produtos:")
        for produto in produtos:
            print(f"Nome do produto: {produto.nome} - Sabor: {produto.sabor}")

    def deletar_produtos(self, produto: any) -> any:
        if not produto:
            print("Produto não encontrado")
            return
        print(f"Produto deletado com sucesso: {produto.nome}")
