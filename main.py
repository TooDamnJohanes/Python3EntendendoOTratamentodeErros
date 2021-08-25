from pprint import pprint
from exceptions import SaldoInsuficienteError
from leitor import LeitorDeArquivo

class CLiente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.proffisao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None
    def __init__(self, cliente, agencia, numero):
        self.__saldo = 0
        self.__agencia = 0
        self.__numero = 0

        self.cliente = cliente
        self.__set__agencia(agencia)
        self.__set__numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30/ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia


    def __set__agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("O ATRIBUTO AGENCIA DEVE SER UM NUMERO INTEIRO")
        if value <= 0:
            raise ValueError("O ATRIBUTO AGENCIA DEVE SER MAIOR QUE ZERO")
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set__numero(self, value):
        if not isinstance(value, int):
            raise ValueError("O ATRIBUTO NUMERO DEVE SER UM NUMERO INTEIRO")
        if value <= 0:
            raise ValueError("O ATRIBUTO NUMERO DEVE SER MAIOR QUE ZERO")
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return
        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor < 0:
            raise ValueError("O VALOR NÃO PODE SER NEGATIVO!")
        if valor > self.__saldo:
            raise SaldoInsuficienteError(self.__saldo, valor)

        self.__saldo -= valor
        favorecido.depositar(valor)

    def sacar(self, valor):
        if valor < 0:
            raise ValueError("O VALOR NÃO PODE SER NEGATIVO!")
        if valor > self.__saldo:
            raise SaldoInsuficienteError(self.__saldo, valor)

        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor


with LeitorDeArquivo("arquivo.txt") as leitor:
    leitor.ler_proxima_linha()
