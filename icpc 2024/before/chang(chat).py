def solveGH(N, M, H, Q, gh, nets, quests):
    nets.sort()

    catch = []
    for xi, yi in gh:
        for lj in nets:
            if H - lj <= yi <= H + lj:
                catch.append(xi)
                nets.remove(lj)
                break

    catch.sort()

    results = []

    for qi in quests:
        if qi > len(catch):
            results.append(-1)
        else:
            results.append(catch[qi - 1])

    return results


def solve():
    N, M, H, Q = map(int, input().split())
    gh = [tuple(map(int, input().split())) for _ in range(N)]
    nets = list(map(int, input().split()))
    quests = [int(input()) for _ in range(Q)]
    results = solveGH(N, M, H, Q, gh, nets, quests)
    print('\n'.join(map(str, results)))


solve()
