def menu():
    print("\n=== BEM VINDO! ===")
    print("O que deseja fazer?")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")
    return input("Escolha uma opção: ").lower()


def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Valor inválido. Tente novamente.")
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: R$ "))

    if numero_saques >= LIMITE_SAQUES:
        print("❌ Limite de saques diários atingido.")
    elif valor > limite:
        print("❌ O valor do saque excede o limite de R$ 500.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")
    else:
        print("❌ Valor inválido.")

    return saldo, extrato, numero_saques


def mostrar_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    print(extrato if extrato else "Nenhuma movimentação.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")


saldo = 2000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu()

    if opcao == "1":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

    elif opcao == "3":
        mostrar_extrato(saldo, extrato)

    elif opcao == "4":
        print("👋 Obrigado por usar nosso banco. Até logo!")
        break

    else:
        print("⚠️ Opção inválida. Tente novamente.")
