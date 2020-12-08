class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = None

    # def setEndereco(self, cep, rua, numero, complemento, bairro, cidade, estado):
    #     self.endereco = Endereco(
    #         cep, rua, numero, complemento, bairro, cidade, estado)

    # def mostraDadosClientes(self):
    #     return print(f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}')


class PessoaFisica(Cliente):
    def __init__(self, nome, telefone, email, cpf):
        super().__init__(nome, telefone, email)
        self.cpf = cpf
            
    def mostraDadosClientes(self):
        return print(f' Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, CPF: {self.cpf}')



class PessoaJuridica(Cliente):
    def __init__(self, nome, telefone, email, cnpj):
        super().__init__(nome, telefone, email)
        self.cnpj = cnpj

    def mostraDadosClientes(self):
        return print(f' Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, CNPJ: {self.cnpj}')


class Endereco:
    def __init__(self, cep, rua, numero, complemento, bairro, cidade, estado):
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def mostraEndereco(self):
        return print(f' Endereço: CEP: {self.cep}, Rua: {self.rua}, Número: {self.numero}, Complemento: {self.complemento}, Bairro: {self.bairro}, Cidade: {self.cidade}, Estado: {self.estado}')