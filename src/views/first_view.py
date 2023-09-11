def introduction_page():
    message = '''
        Sistema Padaria
        
        * 1. Cadastrar Cliente
        * 2. Listar clientes por estado
        * 3. Mostrar Clientes
        * 4. Cadastrar Produto
        * 5. Listar Produtos
        * 6. Deletar produto
        * 7. Sair
    '''

    print(message)
    command = input('Comando: ')

    return command
