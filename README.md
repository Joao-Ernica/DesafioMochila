# Problema da Mochila (Knapsack Problem)

O **Problema da Mochila** (ou *Knapsack Problem*, em inglês) é um desafio fundamental na área de otimização combinatória.

## Exemplo Prático

Suponha que você esteja indo acampar e tem uma mochila com espaço para 20 quilos. Você tem três itens:

| Item           | Valor | Peso (kg) |
|----------------|-------|-----------|
| Lanterna       | 3     | 2         |
| Garrafa térmica| 5     | 4         |
| Saco de dormir | 7     | 5         |

### Como escolher os itens para maximizar o valor total dentro da capacidade da mochila?

|      | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **Nenhum item** | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| **Lanterna** | 0   | 0   | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 3   | 3   |
| **Garaffa termica** | 0   | 0   | 3   | 3   | 5   | 5   | 8   | 8   | 8   | 8   | 8   |
| **Saco de dormir** | 0   | 0   | 3   | 3   | 5   | 7   | 8   | 10  | 10  | 12  | **12**  |

> O algoritmo da mochila encontra a combinação ideal de itens. Ele considera os valores e pesos para determinar quais itens incluir. 

- No exemplo acima, a solução seria levar a garrafa termica e o saco de dormir, **obtendo um valor total de 12.**
- Garrafa termica (5) + Saco de dormir (7) = 12

# Explicação do codigo

## Criação da função mochila

1. Cria uma matriz para armazenar os valores máximos possíveis para cada capacidade
2. Preenche a matriz com os valores máximos possíveis para cada capacidade
3. Identifica os itens selecionados que maximizam o valor total
4. Retorna o valor máximo obtido e os itens selecionados



### Criação da matriz:

```
def mochila(valores, pesos, capacidade):
    n = len(valores)
    matriz = [[0] * (capacidade + 1) for _ in range(n + 1)]
```

- Começa com uma **criação de uma lista** `[0]` e a **multiplica pelo valor da capacidade da mochila  + 1** (ja que a tabela começa com 0), **assim criando a primeira linha de acordo com a quantidade de colunas**
- Depois será criado **uma lista para cada "item" de acordo com a quantidade de valores possiveis** ``for _ in range(n + 1)``
- **Colocando uma lista sobre outra lista**, formando assim uma matriz

## Preenchendo a Matriz

````
for f in range(1, n + 1):
    for w in range(capacidade + 1):
        if pesos[f - 1] <= w:
            matriz[f][w] = max(matriz[f - 1][w], matriz[f - 1][w - pesos[f - 1]] + valores[f - 1])
        else:
            matriz[f][w] = matriz[f - 1][w]
````


- **Para cada item, realizamos as próximas etapas**, começando do segundo item (índice 1): ``for f in range(1, n + 1)``.
- **Para cada capacidade, calculamos o valor máximo que podemos obter**, de 0 a capacidade: ``for w in range(capacidade + 1)``

### Lógica de Preenchimento

- *Verifica se o peso do item atual é menor ou igual à capacidade atual*
    - **Se verdadeiro, calcula o valor máximo entre:**
        - ``matriz[f - 1][w]``: Valor máximo sem incluir o item atual
        - ``matriz[f - 1][w - pesos[f - 1]] + valores[f - 1]``: Valor máximo incluindo o item atual
    - **Se falso, copia o valor máximo da linha anterior** ``(matriz[f - 1][w])``

#### Exemplo de Preenchimento

````
   0    0    0    0    0    0    0    0    0    0    0
   0    0    3    3    3    3    3    3    3    3    3
   0    0    3    3    5    5    8    8    8    8    8
   0    0    3    3    5    7    8   10   10   12   12
````

### Impressão da Tabela de Valores

````
print("Tabela de Valores:")
for row in matriz:
    print(" ".join(f"{val:4}" for val in row))
````

### Descrição:

> Essa parte do código é responsável por **imprimir a tabela de valores da matriz** em um formato legível

``print(" ".join(f"{val:4}" for val in row))``: **imprime cada linha da matriz**, alinhando os valores com 4 espaços de separação

## Identificar os itens

````
itens = []
i, w = n, capacidade
while i > 0 and w > 0:
    if matriz[i][w] != matriz[i - 1][w]:
        itens.append(i - 1)
        w -= pesos[i - 1]
        i -= 1
````

### Descrição:

> Essa parte do código é responsável por **identificar os itens** que devem ser incluídos na mochila para alcançar o **melhor aproveitamento da capacidade da mochila**

- Ela faz isso analisando a matriz de valores, **identificando os itens que contribuem para o valor máximo**

- Se o valor em [i][w] for igual ao valor em [i - 1][w], isso significa que o item i - 1 não adicionou valor algum
- Mas se o valor em [i][w] for maior, isso significa que o item i - 1 foi necessário para alcançar esse valor maior

### Exemplo:

| Capacidade | 0 | 1 | 2 | 3 | 4 | 5 |
|------------|---|---|---|---|---|---|
|      **Nenhum item**    | 0 | 0 | 0 | 0 | 0 | 0 |
|    **Lanterna**        | 0 | 0 | 3 | 3 | 3 | 3 |
|**Garrafa térmica** | 0 | 0 | 3 | 5 | 5 | **8** |
|      **Saco de dormir**      | 0 | 0 | 3 | 5 | 7 | **10** |

> Se você comparar os valores em [2][5] (8) e [3][5] (10), vê que:

- O valor em [3][5] (10) é maior do que o valor em [2][5] (8)
- O item 2 (índice 2) contribuiu para esse aumento de valor

Portanto, o item 2 é necessário para alcançar o valor máximo de 10

E será adicionado na lista:  ``itens.append(i - 1)``

## Parte principal

### Definição dos itens
````
objetos = {
    "Lanterna": {"valor": 3, "peso": 2},
    "Garrafa térmica": {"valor": 5, "peso": 4},
    "Saco de dormir": {"valor": 7, "peso": 5}
}
````
### Valores e pesos

````
valores = [objetos[item]["valor"] for item in objetos]
pesos = [objetos[item]["peso"] for item in objetos]
````

> Irá buscar os valores e pesos do **objetos**
### Capacidade máxima da mochila
> capacidade = 10

### Resolução do problema
> ValorMax, itens = mochila(valores, pesos, capacidade)

### Impressão dos Resultados


````
print(f"Valor máximo obtido: {ValorMax}")
print(f"Índices dos itens selecionados: {itens} (correspondem a: {[list(itens.keys())[i] for i in itens]})")
````

- A primeira linha imprime o valor máximo obtido.
- A segunda linha imprime os índices dos itens selecionados e os nomes correspondentes.


