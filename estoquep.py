codigos = []
nomes = []
quantidades = []
precosuni = []
vendas = []
tra = 130 * "●"
tra2 = 130 * "_"
tra3 = 130 * "x"

while True:
    opcao = input(f"{tra}\n                                                      ● ESCOLHA UMA OPÇÃO: ●\n{tra}\n                                                   1: Adicionar produtos;\n                                                   2: Vender produtos;\n                                                   3: Verificar o estoque atual;\n                                                   4: Calcular o faturamento;\n                                                   5: Limpar histórico;\n                                                   6: Sair do programa;\n{tra}\n")

    if opcao == "1":
        try:
            addcodigo = int(input(f"{tra}\n- Qual é o código do novo cadastro? 🔢: "))
            codigos.append(addcodigo)
            addprodutos = input(f"- Qual é o nome do produto? 🛒: ")
            nomes.append(addprodutos)
            addqnt = int(input("- Qual é a quantidade do produto? 📊: "))
            if addqnt<1:
                print("- É IMPOSSÍVEL CADASTRAR ESSA QUANTIDADE. TENTE NOVAMENTE.")
                break
            quantidades.append(addqnt)
            addpreco = float(input("- Qual é o preço da unidade? 💰: "))
            precosuni.append(addpreco)
            print(f"{tra2}\n\n                                                 🛍️🛍️ PRODUTO CADASTRADO 🛍️🛍️\n")
        except ValueError:
            print(f"\n{tra3}\nERRO, TENTE NOVAMENTE!\n{tra3}\n")

    elif opcao == "2":
        try:
            print(f"{tra}\n- PARA A VENDA: os códigos existentes são {codigos}.\n{tra}")
            cod1 = int(input("● INSIRA O CÓDIGO DO PRODUTO VENDIDO: ")) 
            indice = codigos.index(cod1)
            print(f"{tra}\n- A quantidade disponível é de: {quantidades[indice]} unidades.\n{tra}")
            qntd1 = int(input("● INSIRA A QUANTIDADE VENDIDA: "))

            if cod1 in codigos:
                if qntd1 <= quantidades[indice]:  # Verifica se a quantidade vendida não excede a quantidade em estoque
                    quest = print(f"{tra}\n---> O código {cod1} relaciona-se ao produto {nomes[indice]}. O preço por unidade é de {precosuni[indice]}.\n{tra2}\n                                            🛒🛒 A VENDA FOI CONCLUÍDA COM SUCESSO! 🛒🛒\n{tra2}")
                    conta = quantidades[indice] - qntd1  # Atualiza a quantidade no estoque
                    print(f"\n{tra2}\n                                                 🚨🚨 ESTOQUE ATUALIZADO! 🚨🚨 \n                                             A quantidade atual de {nomes[indice]}, agora é {conta}.\n")
                    quantidades[indice] = conta  # Atualiza a lista de quantidades
                    multiplic = qntd1 * precosuni[indice]
                    vendas.append(multiplic)
                else: 
                    print(f"\n{tra3}\n                                  NÃO TEMOS A QUANTIDADE SOLICITADA, O ESTOQUE POSSUI {quantidades[indice]} UNIDADE(S)\n{tra3}")
            else:
                print(f"\n{tra3}\nTENTE NOVAMENTE!\n{tra3}")

        except ValueError:
            print(f"\n{tra3}\nERRO! INSIRA CARACTERES VÁLIDOS.\n{tra3}\n")

                      
    elif opcao == "3":
        print("Estamos verificando o estoque... 📦📦📦") 
        tabela = list(zip(nomes, precosuni, quantidades))
        print("---> [NOME, VALOR E QUANTIDADE]:")
        for item in tabela:
            print(f"{item[0]}, R${item[1]}, {item[2]}")
        print()
       
                    
    elif opcao == "4":
        print(f"VEJA O EXTRATO ATÉ O MOMENTO: {vendas}.")
        print(f"💵💰📊 O FATURAMENTO, ATÉ AGORA, FOI DE R${sum(vendas):.2f}. 📊💰💵")                    
                      
    elif opcao == "5":
        sn = input("O seu histórico será excluído, você tem certeza? (s/n): ")
        if sn.lower() == "s":
            nomes.clear()
            quantidades.clear()
            codigos.clear()
            precosuni.clear()
            vendas.clear()
            print("Nós limpamos o seu histórico.")
        else:
            print("Operação cancelada. Reinicie o programa! <3")
    else:
        print("--> SAINDO DO PROGRAMA... ATÉ A PRÓXIMA 👋👋")
        break
