class Pedido:
    def __init__(self, codigo, cliente, descricao):
        self.codigo = codigo
        self.cliente = cliente
        self.status = "Efetuado"
        self.descricao = descricao

    def alterarStatus(self, status):
        self.status = status 

    def consultarPedidos(self):
        print(f" Pedido: {self.codigo} \n Cliente: {self.cliente} \n Status: {self.status} \n Descrição: {self.descricao}")
