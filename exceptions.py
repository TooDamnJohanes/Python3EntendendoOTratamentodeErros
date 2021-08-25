class SaldoInsuficienteError(Exception):
    def __init__(self, saldo=None, valor=None):
        self.saldo = saldo
        self.valor = valor
        self.mensagem = 'Saldo insuficiente para efetuar a transação!\n' \
                        f'Saldo atual: {self.saldo} | Valor solicitado de saque: {self.valor}'.upper()
        super(SaldoInsuficienteError, self).__init__(self.mensagem)