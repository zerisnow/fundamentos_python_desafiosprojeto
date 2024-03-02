saldo = 0.0
transacoes = []
saques_diarios = 0

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
        if valor > 0:
            saldo += valor
            transacoes.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    elif opcao == "2":
        if saques_diarios >= 3:
            print("Limite de saques diários atingido.")
            continue

        valor = float(input("Valor do saque: R$ "))
        if valor > 500:
            print("O valor excede o limite de R$ 500,00 por saque.")
            continue

        if saldo >= valor:
            saldo -= valor
            saques_diarios += 1
            transacoes.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    elif opcao == "3":
        if not transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in transacoes:
                print(transacao)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Obrigado por usar o Banco Digital. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")