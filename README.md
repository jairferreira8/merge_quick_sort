# merge_quick_sort

Ideia central: recursividade e dividir para conquistar
O material começa explicando que a recursividade reduz um problema até um caso-base (ex: uma lista com 1 elemento já está ordenada). Diferente da busca binária, que descarta metade dos dados, a ordenação precisa processar tudo — então o problema se divide em duas chamadas simultâneas que depois precisam ser recombinadas

Merge Sort — divisão pela posição

Divide a lista cegamente ao meio (sem olhar os valores), até sobrar listas de 1 elemento.
A parte pesada do trabalho acontece na volta da recursão, na função merge(): compara o menor elemento disponível de cada metade e vai transferindo o menor para o resultado, até esgotar uma das listas (e depois despeja o resto)
Resultado: árvore de recursão sempre perfeitamente balanceada, profundidade ~log₂n.
Complexidade garantida: O(n log n), sempre — não importa a entrada

Quick Sort — divisão pelo valor

Escolhe um pivô (no exemplo, o último elemento) e particiona a lista em três grupos: menores, iguais e maiores que o pivô
O trabalho pesado acontece na descida (particionamento), não na volta — depois disso o pivô já está na posição final correta
Aplica a mesma lógica recursivamente nas partições
Problema: se a lista já estiver ordenada (ou o pivô for sempre o maior/menor valor), o particionamento fica muito desbalanceado — uma partição fica vazia e a outra quase do tamanho original, criando uma árvore "torta" e profunda
Complexidade: O(n log n) no caso típico, mas O(n²) no pior caso

Comparação direta

Aspecto	Merge Sort	Quick Sort
Lógica de divisão	Posição	Valor (pivô)
Operação pesada	Merge (na volta)	Particionamento (na descida)
Complexidade	O(n log n) garantido	O(n log n) típico / O(n²) pior caso

Outros pontos

Como os subproblemas são independentes, dá pra paralelizar com o padrão fork & join (cada metade processada em uma CPU diferente, depois junta o resultado)
Mapa mental final: Recursividade → Dividir e Conquistar → Merge Sort (divide por posição, reconstrói com merge) ou Quick Sort (escolhe pivô, particiona por valor)