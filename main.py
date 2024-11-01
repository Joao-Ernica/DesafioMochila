def mochila(valores, pesos, capacidade):
    n = len(valores)
    matriz = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for f in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[f - 1] <= w:
                matriz[f][w] = max(matriz[f - 1][w], matriz[f - 1][w - pesos[f - 1]] + valores[f - 1])
            else:
                matriz[f][w] = matriz[f - 1][w]

    print("Tabela de Valores:")
    for row in matriz:
        print(" ".join(f"{val:4}" for val in row))  # Alinhar tabela

    # Encontrar os objetos selecionados
    itens = []
    i, w = n, capacidade
    while i > 0 and w > 0:
        if matriz[i][w] != matriz[i - 1][w]:
            itens.append(i - 1)
            w -= pesos[i - 1]
        i -= 1

    return matriz[n][capacidade], itens[::-1]

objetos = {
    "Lanterna": {"valor": 3, "peso": 2},
    "Garrafa térmica": {"valor": 5, "peso": 4},
    "Saco de dormir": {"valor": 7, "peso": 5}
}

valores = [objetos[item]["valor"] for item in objetos]
pesos = [objetos[item]["peso"] for item in objetos]

capacidade = 10

ValorMax, itens = mochila(valores, pesos, capacidade)
print(f"Valor máximo obtido: {ValorMax}")
print(f"Índices dos objetos selecionados: {itens} (correspondem a: {[list(objetos.keys())[i] for i in itens]})")
