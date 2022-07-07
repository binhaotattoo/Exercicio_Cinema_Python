

from operator import length_hint


lugares = []
#Lista = 0
#cont = 0
#x= 0
print("\nBem vindo ao cinema:")
print("___"*18)
quantidadeLugares = int (input("\nDigite a quantidade de cadeiras que pretende reservar:"))
print("___"*18)
print("\nEscolha abaixo qual numero de cadeira quer reservar:")
print("---"*17)

for i in range(quantidadeLugares):
   lugares.append(i+1)
print(lugares)
print("\n")
 
cadeiras = int (input("\nEscolha a cadeira que pretende reservar:"))

while ( lugares [i] != True ):
    
    for i in range(quantidadeLugares):
        if (cadeiras == lugares [i]):
            lugares [i] = "x"
            print("\n") 
                       
        if (lugares [i] =="x"):
            print(lugares)
            print("\n")
       
        if lugares [i] == "x" :
            print("Lugares com (X) está ocupado, escolha outra cadeira")   
                     
    cadeiras = int(input("Escolha a proxima cadeira disponivel:")) 
    print(lugares)
    
    if (cadeiras <= 0):
        print("\n\nVocê digitou (0), não é mais possível escolher cadeiras, bom filme")
        print("Fim")
        break 
#faltando operação de saida para quando  a sala estiver cheia. 
                        
   
    