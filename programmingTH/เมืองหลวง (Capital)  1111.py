import sys
from collections import defaultdict, deque


def main():
    input = sys.stdin.readline
    n = int(input().strip())
    graph = defaultdict(list)

    print(f"จำนวนเมืองทั้งหมด: {n}")
    print("== กำลังอ่านข้อมูลถนน == ")

    for _ in range(n - 1):
        u, v, w = map(int, input().strip().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        print(f"ถนน: {u} <-> {v} (ระยะทาง {w})")

    print("\n== โครงสร้างกราฟ == ")
    for node in graph:
        print(f"เมือง {node} เชื่อมกับ: {graph[node]}")

    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    print(graph)
    q = deque()
    q.append(1)
    visited[1] = True

    print("\n== เริ่ม BFS จากเมือง 1 ==")
    while q:
        u = q.popleft()
        print(f"\nกำลังเยี่ยมเมือง {u} (ระยะทางจากเมือง 1 = {dist[u]})")
        for v, w in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + w
                q.append(v)
                print(f" -> พบเมือง {v} ผ่านถนนระยะ {w} → ระยะรวม: {dist[v]}")

    print("\n== สรุประยะทางทั้งหมดจากเมือง 1 ==")
    for i in range(1, n + 1):
        print(f"เมือง {i}: {dist[i]}")

    print("\n== ผลลัพธ์สุดท้าย ==")
    print(max(dist))


if __name__ == "__main__":
    main()
