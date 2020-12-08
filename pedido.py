class Pedido:
    def __init__(self, codigo, cliente, descricao):
        self.codigo = codigo
        self.cliente = cliente
        self.status = "Efetuado"
        self.descricao = descricao

    def alterarStatus(self, status):
        self.status = status 

    def consultarPedidos(self):
        print(f"Pedido: {self.codigo} \nCliente: {self.cliente} \nStatus: {self.status} \nDescrição: {self.descricao}")
