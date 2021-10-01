
def diagonal_en_Matriz(lista):
    lin_diagonal = []
    for i in range(len(lista)):
        lin_diagonal.append(lista[i][i])
    return(lin_diagonal)

def main():
  
    mat = []
    renglon = []
    reng = int(input(''))
    col = int(input(''))
    if reng != col:
        print('La matriz no es cuadrada')
    else:
        for i in range(reng):
            renglon = []
            for j in range(col):
                a = int(input())
                renglon.append(a)
            mat.append(renglon)
        print(diagonal_en_Matriz(mat))

if __name__=='__main__':
    main()
