from copy import deepcopy

def dfs(cur, graph):
    last = cur[-1]
    check = False
    for g in graph:
        if g[0] == last:
            dfs(cur + " " + g[1], graph)
            check = True
    if check == False:
        print(cur)

def main():
    skills = input().split()

    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(input().split())

    first = deepcopy(skills)
    for g in graph:
        idx = first.index(g[1])
        del first[idx]

    for s in first:
        dfs(s, graph)










if __name__=="__main__":
    main()