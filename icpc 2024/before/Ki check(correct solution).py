def minimum_distance_to_catch_grasshoppers(
        N, M, H, Q, grasshoppers, nets, queries):
    nets.sort()

    catchable_distances = []
    for xi, yi in grasshoppers:
        for lj in nets:
            if H - lj <= yi <= H + lj:
                catchable_distances.append(xi)
                nets.remove(lj)
                break

    catchable_distances.sort()

    results = []
    total_catchable = len(catchable_distances)

    for qi in queries:
        if qi > total_catchable:
            results.append(-1)
        else:
            results.append(catchable_distances[qi - 1])

    return results


N, M, H, Q = map(int, input().split())
grasshoppers = []
for _ in range(N):
    x, y = map(int, input().split())
    grasshoppers.append((x, y))

nets = list(map(int, input().split()))

queries = []
for _ in range(Q):
    qi = int(input())
    queries.append(qi)

results = minimum_distance_to_catch_grasshoppers(
    N, M, H, Q, grasshoppers, nets, queries)
for result in results:
    print(result)
