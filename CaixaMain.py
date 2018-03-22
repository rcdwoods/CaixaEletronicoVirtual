login=["Adm","Richard","Lucas","Yan"]
senha=["Adm","www.123","123456","654321"]
saldo=[0,999999,1299,0,0]
tam=len(login)
n=-1
acesso=0
acessor=0
print("|---------------------------------|")
print("| Bem vindo ao caixa-eletrônico.  |")
print("| Digite uma das opções a seguir: |")
print("|     (1) Login |(2) Cadastro     |")
print("|---------------------------------|")
resposta=(int(input("| Opção: ")))
if(resposta==1):
    print("|----------------------------------")
    print("| Tela de login:\n|")
    tlogin=(input("| Login: "))
    tsenha=(input("| Senha: "))
    print("|----------------------------------")
    while(n<tam-1):
        n=n+1
        if(tlogin==login[n] and tsenha==senha[n]):
            acesso=1
            break
        else:
            acesso=0
    if(acesso==1): #Acesso ao login == 0 == true
        print("| Login efetuado com sucesso.\n|")
        print("| Bem vindo,",login[n],".")
        print("|----------------------------|")
        print("|     Opções disponiveis:    |")
        print("|     (1) Saldo (2) Saque    |")
        print("|----------------------------|")
        opcao= int(input("| Opção: "))
        print("|----------------------------------")
        if(opcao==2):
            valor=(int(input("| Digite o valor para saque: ")))
            resto=1
            if(valor<=saldo[n]):
                saldo[n]=saldo[n]-valor
                while(resto!=0):
                    n50=int(valor/50)
                    resto=int(valor%50)
                    n20=int(resto/20)
                    resto=int(resto%20)
                    n10=int(resto/10)
                    resto=int(resto%10)
                    n5=int(resto/5)
                    resto=int(resto%5)
                    n2=int(resto/2)
                    resto=int(resto%2)
                    print("| Valor total do saque: R$ ",valor,".")
                    print("| Saldo atual: R$ ",saldo[n],"\n|----------------------------------")
                    print("| Notas de 50: ",n50,"")
                    print("| Notas de 20: ",n20,"")
                    print("| Notas de 10: ",n10,"")
                    print("| Notas de 5: ",n5,"")
                    print("| Notas de 2: ",n2)
            else:
                print("| Saldo insuficiente para saque.")
        elif(opcao==1):
            print("|Seu saldo é: R$ ",saldo[n],".")

    else: #Acesso ao login == 0 == false
        print("Login invalido.")
elif(resposta==2):
    print("|----------------------------------")
    print("| Tela de registro:")
    clogin=(input("login: "))
    m=0
    for i in range(tam-1):
        m=m+1
        if(clogin==login[m]):
            acessor=0
            break
        else:
            acessor=1
    if(acessor==0):
        print("| Usuário já registrado.")
    else:
        senhat=(input("| Digite a senha: "))
        senhat2=(input("| Digite a senha novamente: "))
        if(senhat==senhat2):
            login.append(clogin)
            senha.append(senhat)
            saldo.append(0)
            print("| Registrado com sucesso.")
        else:
            print("| Senhas não conferem.")
        
else:
    input("| Opção invalida.\nTecle ENTER para continuar...\n")
