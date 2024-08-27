def min_distance_to_catch_grasshoppers(N, M, H, Q, distance, nets, queries):
    # Sort grasshoppers by distance and nets by length
    distance.sort()
    nets.sort()

    # Create a list of the maximum number of catchable grasshoppers up to each distance
    catchable = [0] * N
    net_index = 0
    current_catchable = 0

    for i in range(N):
        x, y = distance[i]
        
        # Try to find the smallest net that can catch this grasshopper
        while net_index < M and nets[net_index] < abs(H - y):
            net_index += 1
        
        if net_index < M and abs(H - y) <= nets[net_index]:
            current_catchable += 1
            net_index += 1
        
        catchable[i] = current_catchable

    # Determine the minimum distance required for each query
    results = []
    for q in queries:
        if q <= catchable[-1]:
            results.append(distance[q - 1][0])
        else:
            results.append(-1)

    return results

# Input Parsing
N, M, H, Q = map(int, input().split())
distance = [tuple(map(int, input().split())) for _ in range(N)]
nets = list(map(int, input().split()))
queries = [int(input()) for _ in range(Q)]

# Get the results
results = min_distance_to_catch_grasshoppers(N, M, H, Q, distance, nets, queries)

# Output results
for result in results:
    print(result)
