


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

while ( lugares [i] != True ):#quantidadeLugares):
    
    for i in range(quantidadeLugares):
        if (cadeiras == lugares [i]):
            lugares [i] = "x"
            print("\n")
            #print(lugares)    
        if (lugares [i] =="x"):
            print(lugares, ( "\nLugares com X está ocupado, faça uma nova escolha:"))
            print("\n")
    if (cadeiras <= 0):
        print("fim")
        break 

                             
    cadeiras = int(input("\nEscolha a proxima cadeira disponivel")) 
    
 


