
p: list[int] = [25, 24, 15]
w: list[int] = [18, 15, 10]


def mochila_solve(p: list[int], w: list[int], capacidade_mochila: int) -> tuple:

    quantidade_atual: int = 0
    ganho_final: int = 0

    ordena_por_custo(p, w)

    for i in range(len(w)):
        espaco_mochila = capacidade_mochila - quantidade_atual
        if espaco_mochila == 0:
            return (quantidade_atual, ganho_final)
        if espaco_mochila >= w[i]:
            quantidade_atual += w[i]
            ganho_final += p[i]
        else:
            quantidade_atual += espaco_mochila
            ganho_final += (p[i]/w[i]) * espaco_mochila
            return (quantidade_atual, ganho_final)
    return (quantidade_atual, ganho_final)


def ordena_por_custo(p: list[int], w: list[int]) -> None:

    vet: list[float] = []

    for i in range(len(p)):
        vet.append(p[i]/w[i])
    
    aux: float = 0

    for i in range(len(vet)):
        for j in range(len(vet) - 1):
            if vet[j] < vet[j + 1]:
                aux = vet[j]
                vet[j] = vet[j + 1]
                vet[j + 1] = aux
                aux = p[j]
                p[j] = p[j + 1]
                p[j + 1] = aux
                aux = w[j]
                w[j] = w[j + 1]
                w[j + 1] = aux


ganho = mochila_solve(p, w, 20)
print(ganho)
