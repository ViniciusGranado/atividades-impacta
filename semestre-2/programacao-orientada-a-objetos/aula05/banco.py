class Conta:
    def __init__(self, numero, titular) -> None:
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor < 0:
            return "Valor deve ser positivo"

        self.__saldo += valor
        return 'Depósito realizado com sucesso'

    def sacar(self, valor):
        if valor < 0:
            return "Valor deve ser positivo"

        if valor > self.__saldo:
            return 'Saldo insuficiente'

        self.__saldo -= valor
        return 'Saque realizado com sucesso'


conta_1 = Conta(1, 'Vinicius')
print(conta_1.saldo)

print(conta_1.depositar(50))

print(conta_1.saldo)

print(conta_1.depositar(150))

print(conta_1.saldo)

print(conta_1.depositar(-10))

print(conta_1.sacar(50))

print(conta_1.saldo)

print(conta_1.sacar(-50))

print(conta_1.sacar(1000))
