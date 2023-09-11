def introduction_page():
    message = '''
        Sistema Padaria
        
        * 1. Cadastrar Cliente
        * 2. Listar clientes por estado
        * 3. Cadastrar Produto
        * 4. Listar Produtos
        * 5. Deletar produto
        * 6. Cadastrar loja
        * 7. Listar lojas
        * 8. Deletar loja
        * 9. Sair
    '''

    print(message)
    command = input('Comando: ')

    return command
