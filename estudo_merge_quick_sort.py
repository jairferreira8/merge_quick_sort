def merge(esquerda, direita):
    # essa funcao pega duas listas que ja tao ordenadas e junta elas ordenado
    resultado = []
    i = 0
    j = 0

    # vai comparando os dois enquanto sobrar elemento nas duas listas
    while i < len(esquerda) and j < len(direita):
        # pega o menor dos dois e bota no resultado
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # uma das listas ja acabou entao só falta jogar o resto da outra
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def merge_sort(lista):
    # caso base lista com 0 ou 1 elemento ja ta ordenada nao precisa fazer nada
    if len(lista) <= 1:
        return lista

    # divide a lista no meio
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    # chama recursivo pra ordenar cada metade
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    # agora junta as duas metades ja ordenadas
    return merge(esquerda, direita)


def quick_sort(lista):
    # caso base de novo lista pequena ja ta ordenada
    if len(lista) <= 1:
        return lista

    # escolhe o pivo aqui to usando o ultimo elemento da lista
    pivo = lista[-1]

    menores = []
    iguais = []
    maiores = []

    # aqui é o particionamento vai comparando cada item da lista com o pivo
    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento == pivo:
            iguais.append(elemento)
        else:
            maiores.append(elemento)

    # chama de novo pros menores e pros maiores e junta tudo no final
    return quick_sort(menores) + iguais + quick_sort(maiores)


# testando os dois algoritmo
if __name__ == "__main__":
    numeros = [6, 2, 8, 3, 1, 7, 4, 5]

    print("lista original:", numeros)
    print("merge sort:", merge_sort(numeros))
    print("quick sort:", quick_sort(numeros))