
filename = "data/pessoa.csv"
dados = []
whit open(filename, "r") as f:
    header = f.readline().split(',')
    #print('Este é o header:', header)
    
    dados = []
    for linha in f:
        linha = linha.strip()
        linha_lista = linha.split(',')
        linha_dict = {}
        for i in range (len(linha_lista)):
            chave = header[i]
            valor = linha_lista[i]
            linha_dict[chave] = valor
        dados.append (linha_dict)   
          
    print(dados)      
        