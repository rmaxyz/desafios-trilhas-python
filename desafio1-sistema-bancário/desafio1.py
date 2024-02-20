
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

menu = """
    ****************************************************
                        [d] Deposito
                        [s] Saque
                        [e] Extrato
                        [q] Sair
    ****************************************************
    """
    
while True:
        
    opcao = input(menu)
        
    if opcao ==  "d": #Depositar
        valor_deposito = float(input("Valor a ser depositado: "))
            
        if valor_deposito >= 0:
            saldo += valor_deposito
            print("Depósito realizado com sucesso!")
            extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
        else:
            print("Valor inválido!")    
    
    elif opcao == "s": #Saque
        valor_saque = float(input("Valor do saque: "))
        
        if numero_saque <= LIMITE_SAQUE:
            
            if saldo >= valor_saque <= limite:
                saldo -= valor_saque
                numero_saque += 1 
                print("Saque realizado com sucesso!")
                extrato += f"Saque de R$ {valor_saque:.2f}\n"
            else:
                print("Saldo insuficiente ou valor do saque inválido!")
        
        else:
            print("Limite de Saque diário excedido!")        
    
    elif opcao == "e": #Extrato
        if extrato:
            print("\n\n", extrato, "\n\n")
        else:
            print("Não foram realizadas movimentações no extrato.")    
    
    elif opcao == "q": #Sair
        break    
                   
    else:
        print("Opção invalida!")
        
print("Sistema encerrado.")                       