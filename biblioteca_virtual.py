### Inicializacao das listas vazias e declaração de variaveis ###

estante1 = []
estante2 = []

# 1.Estruturas dos menus de opções das estantes e interacao com o usuario

nome = input(("Insira seu nome: "))
print(F"Olá {nome}, seja bem vindo a sua biblioteca virtual! A seguir está o menu principal:" )

# 2. Estrutura do Menu Principal
while True:   
    menu_principal = input("- Opção 1 - Estante 1 \n- Opção 2 - Estante 2\n- Opção 3 - Sair do programa\nAguardando sua escolha....")

 
# 3. Estrutura das condições caso seja a estante1  / Acesso da estante 1
    while  menu_principal == "1":
                print("Acessando o menu da estante 1.....")
                menu_estante1 = input("Opção 1 - Adicionar livros \nOpção 2 - Ver a quantidade de livros \nOpção 3 - Voltar ao Menu Principal\nAguardando sua escolha....")
                if menu_estante1== "1":
                    adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                    estante1.append(adicionar_livros)
                    print(f"livro {adicionar_livros} adicionado com sucesso!")
                    while True:
                        continuar_ad = input("Deseja continua adicionando ou sair?S/N")
                        if continuar_ad == "S": 
                                adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                estante1.append(adicionar_livros)
                                print(f"livro {adicionar_livros}adicionado com sucesso!")
                                break

                        else:
                            print("Voltando para o menu da estante....")
                            break
                                        

                elif menu_estante1 == "2":
                                print(f"Sua estante possui {len(estante1)} livros")    
                                while True:
                                    adicionar_ou_nao = input("Deseja adicionar algum livro ou nao ?S/N")   
                                    if adicionar_ou_nao == "S":
                                        adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                        estante1.append(adicionar_livros)  # append adciona no último indice / Final da fila
                                        print("livro adicionado com sucesso!")
                                    else:
                                        while True: 
                                            deseja_continuar2 = input("Escolha a opcao: \nOpcao 1 - Menu da Estante \nOpcao 2 - Menu Principal\nAguardando sua escolha....")

                                            if deseja_continuar2 == "1":
                                                print("Acessando o menu da estante .....")
                                                menu_estante1 = input("Opção 1 - Adicionar livros \n Opção 2 - Ver a quantidade de livros \n Opção 3 - Voltar ao Menu Principal\nAguardando sua escolha....")
                                                break

                                            elif deseja_continuar2 == "2":
                                                print("Retornando ao menu principal...")
                                                menu_principal = input("- Opção 1 - Estante 1 \n- Opção 2 - Estante 2\n- Opção 3 - Sair do programa\nAguardando sua escolha....")

                                       
                else:
                    print("Retornando ao menu principal....")
                    menu_principal = input("- Opção 1 - Estante 1 \n- Opção 2 - Estante 2\n- Opção 3 - Sair do programa\nAguardando sua escolha....")
    
                
# 4. Estrutura das condições caso seja a estante2 / Acesso a estante 2

    while  menu_principal == "2":
                    print("Acessando o menu da estante 2.....")
                    menu_estante2 = input("Opção 1 - Adicionar livros \nOpção 2 - Ver a quantidade de livros \nOpção 3 - Voltar ao Menu Principal\nAguardando sua escolha....")
                    if menu_estante2== "1":
                                adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                estante2.append(adicionar_livros)
                                print(f"livro {adicionar_livros} adicionado com sucesso!")
                                while True:
                                    continuar_ad = input("Deseja continua adicionando ou sair?S/N")
                                    if continuar_ad == "S": 
                                        adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                        estante1.append(adicionar_livros) # append adciona no último indice / Final da fila
                                        print(f"livro {adicionar_livros}adicionado com sucesso!")
                                    else:
                                        print("Voltando para o menu da estante....")
                                        break


                    elif menu_estante2 == "2":
                                print(f"Sua estante possui {len(estante2)}  livros")    
                                adicionar_ou_nao = input("Deseja adicionar algum livro ou nao ?S/N")   
                                if adicionar_ou_nao == "S":
                                    adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                    estante2.append(adicionar_livros)
                                    print("livro adicionado com sucesso!")
                                else:
                                    while True: 
                                        deseja_continuar2 = input("Escolha a opcao: \nOpcao 1 - Menu da Estante \nOpcao 2 - Menu Principal\nAguardando sua escolha....")

                                        if deseja_continuar2 == "1":
                                            print("Acessando o menu da estante .....")
                                            menu_estante2 = input("Opção 1 - Adicionar livros \n Opção 2 - Ver a quantidade de livros \n Opção 3 - Voltar ao Menu Principal\nAguardando sua escolha....")

                                        elif deseja_continuar2 == "2":
                                            print("Retornando ao menu principal...")
                                            menu_principal = input("- Opção 1 - Estante 1 \n- Opção 2 - Estante 2\n- Opção 3 - Sair do programa\nAguardando sua escolha....")

                                        else:
                                            print("Retornando ao menu principal....")
                                            break
                    else:
                        print("Retornando ao menu principal....")
                        break

# 5 . Estrtura de condicao caso o usario queria sair do sistema    
    else:
        print("Saindo do programa...")  
        break   
       

    
                           
    

                                
                             
                                    
                
                                
                                


                    
                        
                                


                        

      
        
                  
            
                










    

