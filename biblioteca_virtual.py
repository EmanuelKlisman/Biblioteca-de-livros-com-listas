### Inicializacao das listas vazias ###

estante1 = []
estante2 = []

# 1.Estruturas dos menus de opções das estantes e interacao com o usuario

usuario = input(("Insira seu nome: "))
print(F"Olá {usuario}, seja bem vindo a sua biblioteca virtual! A seguir está o menu principal:" )

# 2. Loop Estrutura do Menu Principal

while True:   
    menu_principal = input(\
                        "- Opção 1 - Estante 1 \n"
                        "- Opção 2 - Estante 2\n"
                        "- Opção 3 - Sair do programa\n"
                        "  Aguardando sua escolha....")

 
# 4. Estrutura das condições caso seja a estante1  

    if menu_principal == "1":
                while True:
                    print(f"--------Acessando o menu da estante {menu_principal}--------\n")
                    menu_estante1 = input(    
                                            "1 - Adicionar livros\n"
                                            "2 - Ver quantidade\n"
                                            "3 - Livros adicionados \n"
                                            "Aguardando sua escolha...."
                                        )
                    
# 4.1 - Estrutura de acesso a estante 1 / Adiciona livros

                    if menu_estante1 == "1":
                            while True:
                                adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                estante1.append(adicionar_livros)
                                print(f"livro {adicionar_livros} adicionado com sucesso!")
                        
                                continuar = input("Deseja continuar? S/N")

                                if continuar != "S": # Converte a letra para minuscula 
                                 print("--------Voltando ao menu da estante--------")
                                 break
                                 
# 4.2 - Estrutura de acesso a estante 1 / Quantidade de livros

                    elif menu_estante1 == "2":
                            print(f"Sua estante possui {len(estante1)} livros ")
                            while True:
                                adicionar_livros = input("Deseja adicionar algum livro? S/N")

                                if adicionar_livros == "S":
                                    adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                    estante1.append(adicionar_livros)
                                    print(f"livro {adicionar_livros} adicionado com sucesso!")
                                else:
                                    print("--------Voltando ao menu da estante--------")
                                    break

# 4.3 - Estrutura de acesso a estante 1 / Livros Adicionados

                    elif menu_estante1 == "3":
                            print(f"Seus livros adicionados são:{estante1}")
                            input("Digite qualquer tecla para continuar")
                            print("--------Voltando ao menu da estante--------")
                            print(f"--------Acessando o menu da estante {menu_principal}--------\n")
                            menu_estante1 = input(    
                                            "1 - Adicionar livros\n"
                                            "2 - Ver quantidade\n"
                                            "3 - Livros adicionados \n"
                                            "Aguardando sua escolha...."                   
                                )
                            break             
   

# 5. Estrutura das condições caso seja a estante2

    elif menu_principal == "2":
        while True:
                    print(f"--------Acessando o menu da estante {menu_principal}--------\n")
                    menu_estante2 = input(    
                                            "1 - Adicionar livros\n"
                                            "2 - Ver quantidade\n"
                                            "3 - Livros adicionados \n"
                                            "4 - Voltar ao menu principal\n"
                                            "Aguardando sua escolha...."
                                        )
                    
# 6.1 - Estrutura de acesso a estante 2 / Adiciona livros

                    if menu_estante2 == "1":
                            while True:
                                adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                estante2.append(adicionar_livros)
                                print(f"livro {adicionar_livros} adicionado com sucesso!")
                        
                                continuar = input("Deseja continuar? S/N")

                                if continuar != "S": # Converte a letra para minuscula 
                                 print("--------Voltando ao menu da estante--------")
                                 break
                                 
# 6.2 - Estrutura de acesso a estante 2 / Quantidade de livros

                    elif menu_estante2 == "2":
                            print(f"Sua estante possui {len(estante2)} livros ")
                            while True:
                                adicionar_livros = input("Deseja adicionar algum livro? S/N")

                                if adicionar_livros == "S":
                                    adicionar_livros = input("Digite o livro que você deseja adicionar: ")
                                    estante2.append(adicionar_livros)
                                    print(f"livro {adicionar_livros} adicionado com sucesso!")
                                else:
                                    print("--------Voltando ao menu da estante--------")
                                    break

# 6.3 - Estrutura de acesso a estante 2 / Livros Adicionados

                    elif menu_estante2 == "3":
                        print(estante2)
                        print("--------Voltando ao menu da estante--------")
                        print(f"--------Acessando o menu da estante {menu_principal}--------\n")
                        menu_estante2 = input(    
                                            "1 - Adicionar livros\n"
                                            "2 - Ver quantidade\n"
                                            "3 - Livros adicionados \n"
                                            "4 - Voltar ao menu principal\n"
                                            "Aguardando sua escolha...."
                                            )
                        
        

# 6.4 - Retorno ao menu principal

                    elif menu_estante2 == "4":
                        print("--------Voltando ao menu da principal-------")
                        break
    
                         

# 7 - Saida do sistema
    else:  
     print("Saindo do programa")
     break
