login=["Adm","Richard","Lucas","Yan"]
senha=["Adm","www.123","123456","654321"]
tam=len(login)
n=0
acesso=0
acessor=0
print("|---------------------------------|")
print("| Bem vindo ao caixa-eletrônico.  |")
print("| Digite uma das opções a seguir: |")
print("|     (1) Login |(2) Cadastro     |")
print("|---------------------------------|")
resposta=(int(input("Opção: ")))
if(resposta==1):
    print("-----------------------------------")
    print("Tela de login:")
    tlogin=(input("Login:"))
    tsenha=(input("Senha:"))
    while(n<tam-1):
        n=n+1
        if(tlogin==login[n] and tsenha==senha[n]):
            acesso=1
            break
        else:
            acesso=0
    if(acesso==1):
        print("Login efetuado com sucesso.")
    else:
        print("Login invalido.")
elif(resposta==2):
    print("-----------------------------------")
    print("Tela de registro:")
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
        print("Usuário já registrado.")
    else:
        senhat=(input("Digite a senha: "))
        senhat2=(input("Digite a senha novamente: "))
        if(senhat==senhat2):
            login.append(clogin)
            senha.append(senhat)
            print("Registrado com sucesso.")
        else:
            print("Senhas não conferem.")
        
else:
    input("Opção invalida.\nTecle ENTER para continuar...\n")
