from cliente import PessoaFisica
from cliente import PessoaJuridica
from cliente import Endereco
from pedido import Pedido

menu = ''' \n Menu
    1-  Cadastrar clientes
    2-	Cadastrar pedidos
    3-  Visualizar clientes cadastrados
    4-  Visualizar pedidos
    5-  Alterar status do pedido
    6-  Encerrar
 Escolha: '''

subMenuPedidos = ''' \n Opções
    1-  Visualizar todos os pedidos
    2-	Visualizar pedido pelo código
    3-  Visualizar pedidos de cliente especifico
    4-  Realizar novo pedido
    5-  Sair
 Escolha: '''

usuarios = []
enderecos = []

pedidos = []

usuario = PessoaFisica('Gian Lucas', '51985422161', 'gian@gmail.com', '86252780006')
usuarios.append(usuario)
endereco = Endereco('91160383', 'Travessa São Jorge', 2, '', 'Santa Rosa', 'Porto Alegre', 'Rio Grande do sul')
enderecos.append(endereco)
usuario = PessoaJuridica('Lucas Quinhones', '51984977634', 'lucas.quinhones@gmail.com', '12345678910123')
usuarios.append(usuario)
endereco = Endereco('91160211', 'Rua Luiz Mandelli', 2, 'Em frente a Igreja', 'Rubem Berta', 'Porto Alegre', 'Rio Grande do sul')
enderecos.append(endereco)

pedido = Pedido(111, 'Gian Lucas', 'Jeans Azul')
pedidos.append(pedido)
pedido = Pedido(222, 'Lucas Quinhones', 'Jaqueta Amarelada')
pedidos.append(pedido)

# Opção 1
def cadastraClientes():
    # Faz a validação do nome
    while True:
        nome = str(input(' Digite o nome do cliente: '))
        if nome == '':
            print(' \n O nome é obrigatório!\n')
        elif len(nome) < 3:
            print(' \n O nome deve ter mais de dois digítos\n')
        else:
            break
    telefone = str(input(' Digite o telefone do cliente: '))
    email = str(input(' Digite o email do cliente: '))

    # Faz a validação dos dados do CPF ou CNPJ:
    while True:
        validaPessoaTipo = int(input(' Digite (1) para cadastrar como Pessoa Fisica ou (2) para cadastrar como Pessoa Juridica: '))
        if validaPessoaTipo == 1:
            while True:
                validaCpf = str(input(' Digite o CPF do cliente: '))
                if len(validaCpf) > 11 or len(validaCpf) < 11:
                    print(' \n O CPF precisa ter 11 digítos! Somente números.\n')
                elif validaCpf == '':
                    print(' \n Valor do CPF não pode ser vazio!\n')
                else:
                    cpf = validaCpf
                    break
            usuario = PessoaFisica(nome, telefone, email, cpf)
            break
        elif validaPessoaTipo == 2:
            while True:
                validaCnpj = str(input(' Digite o CNPJ do cliente: '))
                if len(validaCnpj) > 14 or len(validaCnpj) < 14:
                    cnpj = validaCnpj
                    break
                elif validaCnpj == '':
                    print(' Valor do CNPJ não pode ser vazio!')
                else:
                    print(' O CNPJ precisa ter 14 digítos! Somente números.')
            usuario = PessoaJuridica(nome, telefone, email, cnpj)
            break
        else:
            print(' Valor digitado incorreto! Digite novamente.')

    # Adiciona a instância do Objeto na lista:
    usuarios.append(usuario)

    # Começa a passar os dados de endereço:
    print('\n Passe os dados de endereço:\n')
    cep = str(input(' CEP: '))
    rua = str(input(' Rua: '))
    numero = int(input(' Número da residência: '))
    complemento = str(input(' Complemento: '))
    bairro = str(input(' Bairro: '))
    cidade = str(input(' Cidade: '))
    estado = str(input(' Estado: '))
    endereco = Endereco(cep, rua, numero, complemento, bairro, cidade, estado)
    enderecos.append(endereco)

# Opção 2
def cadastraPedidos():
    cadastraNovoCliente = False
    while True:
        # Valida se o código do pedido está correto com o padrão do sistema:
        while True:
            validaCodigo = str(input(' Digite o código do pedido: '))
            if len(validaCodigo) == 3:
                codigo = int(validaCodigo)
                break
            elif len(validaCodigo) > 3 or len(validaCodigo) < 3:
                print(' \n Código do pedido deve possuir 3 números\n')
            else:
                print(' \n Código do produto deve ser um número de 3 digítos\n')

        # Valida se o cliente digitado existe no sistema:
        validadorCliente = False
        while True:
            validaCliente = str(input(' Digite o cliente que efetuou o pedido: '))
            for usuario in usuarios:
                if validaCliente == usuario.nome:
                    cliente = str(validaCliente)
                    validadorCliente = True
                else:
                    pass
            if validadorCliente == True:
                break
            else:
                print(' \n Cliente digitado não foi encontrado no sistema!\n')
                validaEscolhaIncluirCliente = str(input(' Gostaria de incluir cliente novo no sistema? (S/N) ')).upper()
                if validaEscolhaIncluirCliente == 'S':
                    cadastraClientes()
                    cadastraNovoCliente = True
                    break
                elif validaEscolhaIncluirCliente == 'N':
                    pass
                else:
                    print(' Opção escolhida incorreta')
        if cadastraNovoCliente == True:
            break
        else:
            # Insere os outros dados
            descricao = str(input(' Digite uma descrição do pedido: '))
            pedido = Pedido(codigo, cliente, descricao)
            pedidos.append(pedido)
            break

# Opção 3
def relatorioClientes():
    if len(usuarios) > 0:
        # Apresenta os dados do usuario e o endereço abaixo:
        for chaveUser, usuario in enumerate(usuarios):
            for chaveEnder, endereco in enumerate(enderecos):
                if chaveUser == chaveEnder:
                    usuario.mostraDadosClientes()
                    endereco.mostraEndereco()
                    print()
                else:
                    pass
    else:
        print(' Ainda não possui clientes cadastrados')


# Opção 4
def relatorioPedidos():
    if len(pedidos) > 0:
        validadorPedidoCodigo = False
        while True:
            menuPedido = int(input(subMenuPedidos))
            print()
            # Valida se foi escolhida a opção de mostrar todos os pedidos:
            if menuPedido == 1:
                for pedido in pedidos:
                    pedido.consultarPedidos()
                    print('------------------')

            # Valida se foi escolhida a opção de mostrar pedido a partir do código:
            elif menuPedido == 2:
                codigoPedido = int(input(' Digite o código do pedido: '))
                print()
                for pedido in pedidos:
                    if pedido.codigo == codigoPedido:
                        pedido.consultarPedidos()
                        validadorPedidoCodigo = True
                        print('------------------')
                    else:
                        pass
                if validadorPedidoCodigo == True:
                    pass
                else:
                    print(' Código digitado não encontrado no sistema')

            # Valida se foi escolhida a opção de mostrar os pedidos do cliente especificado:
            elif menuPedido == 3:
                cliente = str(input(' Digite o nome do cliente: '))
                print()
                for pedido in pedidos:
                    if pedido.cliente == cliente:
                        pedido.consultarPedidos()
                        print('------------------')
                    else:
                        pass
            
            # Valida se foi escolhia a opção de cadastrar novo pedido:
            elif menuPedido == 4:
                cadastraPedidos()

            # Valida se foi escolhida a opção de sair das opções de pedido:
            elif menuPedido == 5:
                break

            # Valida se o valor digitado foi incorreto:
            else:
                print(' Valor digitado incorreto!')
    else:
        print(' Ainda não possui pedidos cadastrados')



# Opção 5
def alteraStatus():
    codigoPedido = int(input(' Digite o código do pedido que gostaria de mudar o status: '))
    for pedido in pedidos:
        # Verifica se o valor digitado existe no sistema
        if codigoPedido == pedido.codigo:
            while True:
                novoStatus = int(input(' Escolha o novo status: \n 1 -  Produção \n 2 -  Concluído \n 3 -  Cancelado\n Escolha: '))
                if novoStatus == 1:
                    status = 'Produção'
                    pedido.alterarStatus(status)
                    # validaOk = True
                    break
                elif novoStatus == 2:
                    status = 'Concluído'
                    pedido.alterarStatus(status)
                    # validaOk = True
                    break
                elif novoStatus == 3:
                    status = 'Cancelado'
                    pedido.alterarStatus(status)
                    # validaOk = True
                    break
                else:
                    print(' Opção incorreta, tente novamente!')
        else:
            pass
    print('\n Status do pedido alterado')


while True:
    escolha = input(menu)
    if escolha == '1':
        print("\n Cadastrar clientes")
        cadastraClientes()          
    elif escolha == '2':
        print("\n Cadastrar pedidos \n --------")
        cadastraPedidos()
    elif escolha == '3':
        print("\n Visualizar clientes salvos no sistema\n")
        relatorioClientes()
    elif escolha == '4':
        print("\n Visualizar pedidos")
        relatorioPedidos()
    elif escolha == '5':
        print("\n Alterar status de pedido \n")
        alteraStatus()
    elif escolha == '6':
        sair = str(input('Tem certeza que deseja encerrar a sessão? (S/N) '))
        if sair == 'S' or sair =='s' or sair == 'sim' or sair == 'Sim':
            print(' Obrigado até a próxima!')
            break
        else:
            pass
    else:
        print(' Valor digitado incorreto.')

