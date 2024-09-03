class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular  # Atributo "privado"
        self._saldo = saldo_inicial  # Atributo "privado"

    # Método acessor (getter) para o saldo
    def get_saldo(self):
        return self._saldo

    # Método modificador (setter) para o saldo
    def depositar(self, quantia):
        if quantia > 0:
            self._saldo += quantia
        else:
            print("A quantia de depósito deve ser positiva.")

    # Método modificador para sacar dinheiro
    def sacar(self, quantia):
        if quantia > 0:
            if self._saldo >= quantia:
                self._saldo -= quantia
            else:
                print("Saldo insuficiente.")
        else:
            print("A quantia de saque deve ser positiva.")

    # Método acessor para o titular
    def get_titular(self):
        return self._titular

    # Método modificador para o titular
    def set_titular(self, novo_titular):
        if isinstance(novo_titular, str) and novo_titular:
            self._titular = novo_titular
        else:
            print("Nome do titular deve ser uma string não vazia.")

# Exemplo de uso
if __name__ == "__main__":
    conta = ContaBancaria("João", 1000)
    print(f"Titular: {conta.get_titular()}")
    print(f"Saldo inicial: {conta.get_saldo()}")

    conta.depositar(500)
    print(f"Saldo após depósito: {conta.get_saldo()}")

    conta.sacar(300)
    print(f"Saldo após saque: {conta.get_saldo()}")

    conta.sacar(1500)  # Tentativa de saque com saldo insuficiente
    conta.depositar(-100)  # Tentativa de depósito com quantia negativa
