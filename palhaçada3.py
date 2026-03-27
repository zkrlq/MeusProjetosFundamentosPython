def verificar_condutor():
    # Autor: Enzo
    # Projeto: Verificação de Condutor

    while True:
        # Entrada de dados
        cnh = input("\nO Condutor possui CNH? (sim/nao): ").lower() # .lower() evita erro com 'Sim' ou 'SIM'
        bafometro = float(input("Qual o valor do bafômetro?: "))
    
        # Verificação usando 'in'
        if cnh in ['sim', 's'] and bafometro <= 0.04:
            print("O condutor está habilitado e dentro do limite legal.")
        elif cnh in ['nao', 'n'] and bafometro <= 0.04:
            print("O condutor NÃO possui CNH, mas está dentro do limite legal.")
        elif cnh in ['sim', 's'] and bafometro > 0.04:
            print("O condutor possui CNH, mas está ACIMA do limite legal!")
        elif cnh in ['nao', 'n'] and bafometro > 0.04:
            print("O condutor NÃO possui CNH e está ACIMA do limite legal!")
        else:
            print("Entrada de CNH inválida.")

        # Pergunta movida para fora do else para rodar em cada ciclo
        resposta = input("\nDeseja verificar outro condutor? (s/n): ").lower()
        if resposta not in ['sim', 's']:
            print("Encerrando programa...")
            break

# Chamada da função
verificar_condutor()
