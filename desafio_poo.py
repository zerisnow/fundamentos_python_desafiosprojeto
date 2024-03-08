class BancoDigital:
    def __init__(self):
        self.__saldo = 0.0
        self.__transacoes = []
        self.__saques_diarios = 0

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__transacoes.append(f"Depósito: R$ {valor:.2f}")
            return True
        else:
            return False

    def saque(self, valor):
        if self.__saques_diarios >= 3:
            return False

        if valor > 500:
            return False

        if self.__saldo >= valor:
            self.__saldo -= valor
            self.__saques_diarios += 1
            self.__transacoes.append(f"Saque: R$ {valor:.2f}")
            return True
        else:
            return False

    def extrato(self):
        if not self.__transacoes:
            return "Não foram realizadas movimentações."
        else:
            extrato = ""
            for transacao in self.__transacoes:
                extrato += transacao + "\n"
            extrato += f"Saldo atual: R$ {self.__saldo:.2f}"
            return extrato


banco = BancoDigital()

while True:
    print("\nBem-vindo ao seu Banco Digital!")
    print("Escolha uma opção:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: R$ "))
        if banco.deposito(valor):
            print("Depósito realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    elif opcao == "2":
        valor = float(input("Valor do saque: R$ "))
        if banco.saque(valor):
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente ou limite de saques diários atingido.")

    elif opcao == "3":
        print(banco.extrato())

    elif opcao == "4":
        print("Obrigado por usar o Banco Digital. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")