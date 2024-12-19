import random
from heapq import heappop, heappush
from collections import deque
# Função para gerar o labirinto
def generate_labirinto():
    labirinto = [[0 for _ in range(10)] for _ in range(10)]

    # Adicionar obstáculos
    obstacles = random.sample([(i, j) for i in range(10) for j in range(10) if (i, j) not in [(0, 0), (9, 9)]], random.randint(10, 25))
    for i, j in obstacles:
        labirinto[i][j] = 1

    # Adicionar pontos de recarga
    recharge_5 = random.sample([(i, j) for i in range(10) for j in range(10) if labirinto[i][j] == 0], 5)
    recharge_10 = random.sample([(i, j) for i in range(10) for j in range(10) if labirinto[i][j] == 0 and (i, j) not in recharge_5], 3)
    for i, j in recharge_5:
        labirinto[i][j] = 5
    for i, j in recharge_10:
        labirinto[i][j] = 10

    return labirinto

# Algoritmo de Busca em Largura (BFS)
def bfs(labirinto):
    start = (0, 0, 50) 
    queue = deque([start])
    visited = set()
    visited.add((0, 0))
    path = []

    while queue:
        x, y, energy = queue.popleft()

      
        if (x, y) == (9, 9):
            path.append((x, y))
            return path

        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in visited:
                if labirinto[nx][ny] != 1:  
                    new_energy = energy - 1
                    if labirinto[nx][ny] == 5:
                        new_energy += 5
                    elif labirinto[nx][ny] == 10:
                        new_energy += 10

                    if new_energy > 0:
                        queue.append((nx, ny, new_energy))
                        visited.add((nx, ny))
                        path.append((x, y))
    return []

# Algoritmo de Busca A*
def a_star(labirinto):
    def heuristic(x, y):
        return abs(x - 9) + abs(y - 9)

    start = (0, 0, 50)
    queue = [(0 + heuristic(0, 0), 0, 0, 50, [])]
    visited = set()

    while queue:
        _, x, y, energy, path = heappop(queue)

       
        if (x, y) == (9, 9):
            return path + [(x, y)]

        if (x, y) in visited:
            continue
        visited.add((x, y))

       
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in visited:
                if labirinto[nx][ny] != 1:
                    new_energy = energy - 1
                    if labirinto[nx][ny] == 5:
                        new_energy += 5
                    elif labirinto[nx][ny] == 10:
                        new_energy += 10

                    if new_energy > 0:
                        heappush(queue, (len(path) + 1 + heuristic(nx, ny), nx, ny, new_energy, path + [(x, y)]))
    return []

# Função para executar e mostrar resultados
def main():
    labirinto = generate_labirinto()

    print("Labirinto gerado:")
    for linha in labirinto:
        print(" ".join(f"{celula:2}" for celula in linha))

    print("\nBusca em Largura (BFS):")
    caminho_bfs = bfs(labirinto)
    if caminho_bfs:
        print("Caminho encontrado pelo BFS:", caminho_bfs)
    else:
        print("Nenhum caminho encontrado pelo BFS.")

    print("\nBusca A*:")
    caminho_a_star = a_star(labirinto)
    if caminho_a_star:
        print("Caminho encontrado pelo A*:", caminho_a_star)
    else:
        print("Nenhum caminho encontrado pelo A*.")


if __name__ == "__main__":
    main()