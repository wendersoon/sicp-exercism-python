def trianguloPascal(n):
    lista = [[1],[1,1]]
    for i in range(1,int(n)):
        linha = [1]
        for j in range(0,len(lista[i])-1):
            linha += [ lista[i][j] + lista[i][j+1] ]
        linha += [1]
        lista += [linha]
    return lista

n = input("Enter the number of rows for Pascal's triangle: ")
resultado = trianguloPascal(n)

for i in range(len(resultado)):
    print(resultado[i])