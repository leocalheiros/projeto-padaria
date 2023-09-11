class LojaView:
    def cadastrar_loja(self, nome: str) -> None:
        print(f"Loja cadastrada com sucesso: {nome}")

    def mostrar_lojas(self, lojas) -> None:
        if not lojas:
            print("Nenhuma loja encontrada")
            return
        print("Lojas:")
        for loja in lojas:
            print(f"Nome da loja: {loja.nome}")

    def deletar_loja(self, nome: str) -> None:
        print(f"Loja deletada com sucesso: {nome}")
