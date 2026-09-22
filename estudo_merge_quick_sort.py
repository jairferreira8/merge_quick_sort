def merge(esquerda, direita):
    """Combina duas listas já ordenadas em uma única lista ordenada."""
    resultado = []
    i = 0
    j = 0

    # Enquanto ainda houver elementos nas duas listas
    while i < len(esquerda) and j < len(direita):
        # Copia o menor elemento disponível
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Uma das listas terminou.
    # Acrescenta os elementos restantes da outra.
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


def merge_sort(lista):
    """Ordena a lista dividindo-a recursivamente pela posição (ao meio)."""
    # Caso-base: lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return lista

    # Divisão: corta a lista em duas metades
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    # Recursão: ordena cada metade
    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    # Combinação: intercala as duas metades já ordenadas
    return merge(esquerda, direita)


def quick_sort(lista):
    """Ordena a lista escolhendo um pivô e particionando pelo valor."""
    # Caso-base: lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return lista

    # Escolha do pivô: último elemento da lista
    pivo = lista[-1]

    menores = []
    iguais = []
    maiores = []

    # Particionamento: compara cada elemento com o pivô
    for elemento in lista:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento == pivo:
            iguais.append(elemento)
        else:
            maiores.append(elemento)

    # Recursão: ordena as partições e junta tudo
    return quick_sort(menores) + iguais + quick_sort(maiores)


# --- Exemplo de uso ---
if __name__ == "__main__":
    numeros = [6, 2, 8, 3, 1, 7, 4, 5]

    print("Lista original:", numeros)
    print("Merge Sort:", merge_sort(numeros))
    print("Quick Sort:", quick_sort(numeros))