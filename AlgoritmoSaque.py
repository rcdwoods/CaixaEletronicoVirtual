print("|---------------------------------|")
print("| Bem vindo ao caixa-eletrônico.  |")
print("| 	      Saques		  |")
print("|            		          |")
print("|---------------------------------|")
valor=(int(input("Digite o valor para saque: ")))
resto=1
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
    print("Valor total do saque: ",valor,"\n")
    print("Notas de 50: ",n50,"\n")
    print("Notas de 20: ",n20,"\n")
    print("Notas de 10: ",n10,"\n")
    print("Notas de 5: ",n5,"\n")
    print("Notas de 2: ",n2)
