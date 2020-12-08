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
    6-  Altera dados do cliente
    7-  Remove cliente
    8-  Encerrar
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

usuario = PessoaFisica('Gian Lucas', '51985422161',
                       'gian@gmail.com', '86252780006')
usuarios.append(usuario)
endereco = Endereco('91160383', 'Travessa São Jorge', 2, '',
                    'Santa Rosa', 'Porto Alegre', 'Rio Grande do sul')
enderecos.append(endereco)
usuario = PessoaJuridica('Lucas Quinhones', '51984977634',
                         'lucas.quinhones@gmail.com', '12345678910123')
usuarios.append(usuario)
endereco = Endereco('91160211', 'Rua Luiz Mandelli', 2, 'Em frente a Igreja',
                    'Rubem Berta', 'Porto Alegre', 'Rio Grande do sul')
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

    # Faz a validação do telefone
    while True:
        validaTelefone = str(input(' Digite o telefone do cliente: '))
        if len(validaTelefone) > 8 and validaTelefone.isdigit():
            telefone = validaTelefone
            break
        else:
            print('\n O telefone deve possuir no minimo 9 digítos, somente números.\n')

    # Faz a validação do email
    while True:
        validaEmail = str(input(' Digite o email do cliente: '))
        if len(validaEmail) > 0:
            email = validaEmail
            break
        else:
            print('\n O email não pode ser vazio.\n')

    # Faz a validação dos dados do CPF ou CNPJ:
    while True:
        validaPessoaTipo = int(input(
            ' Digite (1) para cadastrar como Pessoa Fisica ou (2) para cadastrar como Pessoa Juridica: '))
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
                    print(' O CNPJ precisa ter 14 digítos! Somente números.')
                elif validaCnpj == '':
                    print(' Valor do CNPJ não pode ser vazio!')
                else:
                    cnpj = validaCnpj
                    break
            usuario = PessoaJuridica(nome, telefone, email, cnpj)
            break
        else:
            print(' Valor digitado incorreto! Digite novamente.')

    # Adiciona a instância do Objeto na lista:
    usuarios.append(usuario)

    # Começa a passar os dados de endereço:
    print('\n Passe os dados de endereço:\n')

    # Valida se os dados do CEO estão corretos:
    while True:
        validaCep = str(input(' CEP: '))
        if len(validaCep) > 8 or len(validaCep) < 8:
            print(' \n O CEP deve possuir 8 digítos, somente números.\n')
        else:
            cep = validaCep
            break

    # Valida se os dados da rua estão certos:
    while True:
        validaRua = str(input(' Rua: '))
        if len(validaRua) > 0:
            rua = validaRua
            break
        else:
            print(' \n O nome da rua não pode ser vázio.\n')

    # Valida se o número passado está correto:
    while True:
        validaNumero = str(input(' Número da residência: '))
        if len(validaNumero) > 0 and validaNumero.isdigit() == True:
            numero = int(validaNumero)
            break
        elif validaNumero.isdigit() == False:
            print(' \n Deve conter somente números.\n')
        else:
            print(' \n Número não pode ser vázio.\n')

    complemento = str(input(' Complemento: '))

    # Valida se o bairro digitado não está vázio:
    while True:
        validaBairro = str(input(' Bairro: '))
        if len(validaBairro) > 0:
            bairro = validaBairro
            break
        else:
            print(' \n Bairro não pode ser vázio.\n')

    # Valida se a cidade digitada não está vázia:
    while True:
        validaCidade = str(input(' Cidade: '))
        if len(validaCidade) > 0:
            cidade = validaCidade
            break
        else:
            print(' \n Cidade não pode ser vázio.\n')

    # Valida se o estado digitado não está vázio:
    while True:
        validaEstado = str(input(' Estado: '))
        if len(validaEstado) > 0:
            estado = validaEstado
            break
        else:
            print(' \n Estado não pode ser vázio\n')

    # Adiciona os dados ao Objeto endereco:
    endereco = Endereco(cep, rua, numero, complemento, bairro, cidade, estado)
    # Adiciona a lista de endereços:
    enderecos.append(endereco)

# Opção 2


def cadastraPedidos():
    if len(usuarios) > 0:
        cadastraNovoCliente = False
        while True:
            # Valida se o código do pedido está correto com o padrão do sistema:
            while True:
                validaCodigo = str(input(' Digite o código do pedido: '))
                if len(validaCodigo) == 3:
                    pedidoDuplicado = False
                    for pedido in pedidos:
                        if int(validaCodigo) == pedido.codigo:
                            pedidoDuplicado = True
                            print(
                                ' \n O código do pedido deve ser único, o código digitado já se encontra no sistema.\n')
                        else:
                            pass
                    if pedidoDuplicado == True:
                        pass
                    else:
                        codigo = int(validaCodigo)
                        break
                elif len(validaCodigo) > 3 or len(validaCodigo) < 3:
                    print(' \n Código do pedido deve possuir 3 números\n')
                else:
                    print(' \n Código do produto deve ser um número de 3 digítos\n')

            # Valida se o cliente digitado existe no sistema:
            validadorCliente = False
            while True:
                validaCliente = str(
                    input(' Digite o cliente que efetuou o pedido: '))
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
                    validaEscolhaIncluirCliente = str(
                        input(' Gostaria de incluir cliente novo no sistema? (S/N) ')).upper()
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
    else:
        print('\n Não é possível cadastrar pedido sem ter clientes cadastrados')

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
        print(' \n Ainda não possui pedidos cadastrados')


# Opção 5
def alteraStatus():
    if len(pedidos) > 0:
        codigoPedido = int(
            input(' Digite o código do pedido que gostaria de mudar o status: '))
        for pedido in pedidos:
            # Verifica se o valor digitado existe no sistema
            if codigoPedido == pedido.codigo:
                while True:
                    novoStatus = int(input(
                        ' Escolha o novo status: \n 1 -  Produção \n 2 -  Concluído \n 3 -  Cancelado\n Escolha: '))
                    if novoStatus == 1:
                        status = 'Produção'
                        pedido.alterarStatus(status)
                        break
                    elif novoStatus == 2:
                        status = 'Concluído'
                        pedido.alterarStatus(status)
                        break
                    elif novoStatus == 3:
                        status = 'Cancelado'
                        pedido.alterarStatus(status)
                        break
                    else:
                        print(' Opção incorreta, tente novamente!')
            else:
                pass
        print('\n Status do pedido alterado')
    else:
        print(' \n Ainda não possui pedidos cadastrados')

# Opção 6


def alteraDadosCliente():
    if len(usuarios) > 0:
        validaSaida = False
        usuarioDigitado = str(input(' Digite o nome do cliente: '))
        for cliente in usuarios:
            if usuarioDigitado == cliente.nome:
                # Faz a validação do nome
                while True:
                    nome = str(input(' \n Digite o novo para nome o cliente: '))
                    if nome == '':
                        print(' \n O nome é obrigatório!\n')
                    elif len(nome) < 3:
                        print(' \n O nome deve ter mais de dois digítos\n')
                    else:
                        break
              # Faz a validação do telefone
                while True:
                    validaTelefone = str(
                        input(' Digite o novo telefone para o cliente: '))
                    if len(validaTelefone) > 8 and validaTelefone.isdigit():
                        telefone = validaTelefone
                        break
                    else:
                        print(
                            '\n O telefone deve possuir no minimo 9 digítos, somente números.\n')
                # Faz a validação do email
                while True:
                    validaEmail = str(input(' Digite o novo email para o cliente: '))
                    if len(validaEmail) > 0:
                        email = validaEmail
                        break
                    else:
                        print('\n O email não pode ser vazio.\n')
                        cliente.alteraDados()
                validaSaida = True
                # Altera os dados:
                cliente.alteraDados(nome, telefone, email)
            else:
                pass
        if validaSaida == True:
            print('\n Dados do cliente alterado com sucesso.\n')
        else:
            print('\n Cliente não encontrado no sistema.\n')
    else:
        print(' Ainda não possui clientes cadastrados')

# Opção 6


def removeCliente():
    if len(usuarios) > 0:
        validaRemovido = False
        usuarioDigitado = str(input(' Digite o cliente que deseja excluir: '))
        for chave, cliente in enumerate(usuarios):
            if usuarioDigitado == cliente.nome:
                usuarios.pop(chave)
                validaRemovido = True
            else:
                pass
        if validaRemovido == True:
            print(' \n Cliente removido com sucesso.\n')
        else:
            print(' \n Cliente não encontrado no sistema.\n')
    else:
        print(' Ainda não possui clientes cadastrados')


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
        print("\n Alterar status de pedido")
        alteraStatus()
    elif escolha == '6':
        print("\n Alterar dados do cliente")
        alteraDadosCliente()
    elif escolha == '7':
        print("\n Alterar dados do cliente")
        removeCliente()
    elif escolha == '8':
        sair = str(input(' Tem certeza que deseja encerrar a sessão? (S/N) '))
        if sair == 'S' or sair == 's' or sair == 'sim' or sair == 'Sim':
            print('\n Obrigado até a próxima!')
            break
        else:
            pass
    else:
        print('\n Valor digitado incorreto.')
