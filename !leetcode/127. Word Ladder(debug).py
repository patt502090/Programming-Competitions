from typing import List  # สำหรับประกาศ type hint เช่น List[str]
from collections import defaultdict, deque  # defaultdict ช่วยให้สร้าง dict ที่มีค่า default ได้ / deque ใช้เป็น queue แบบมีประสิทธิภาพสูง

# array[start:end:step] เป็น syntax slicing ทั่วไป เช่น [1:5] เอาตำแหน่ง 1 ถึง 4

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # เงื่อนไขพิเศษ: ถ้า begin == end และ end ไม่อยู่ใน wordList → ไม่มีทางแปลงได้
        if beginWord == endWord and endWord not in wordList:
            return 0

        # graph จะเก็บ key = pattern เช่น "h*t", "*ot", "ho*" → value = คำที่ match กับ pattern นั้น
        graph = defaultdict(list)

        print("=== Building Pattern Graph ===")
        # สร้าง pattern ของทุกคำใน wordList
        for word in wordList:
            for i in range(len(word)):
                tf = word[:i] + "*" + word[i + 1:]  # แปลงตำแหน่งที่ i ให้เป็น "*" เช่น "hot" → "*ot", "h*t", "ho*"
                graph[tf].append(word)  # เพิ่มคำเข้า list ของ pattern นั้น
                print(f"Added pattern: {tf} → {word}")
        print("=== Pattern Graph ===")
        for pattern, words in graph.items():
            print(f"{pattern} → {words}")
        print("=====================")

        # เริ่ม BFS โดยใช้ queue เก็บ (word, current_distance)
        queue = deque([(beginWord, 1)])  # ระยะเริ่มต้น = 1 (เพราะเริ่มจาก beginWord แล้วนับคำด้วย)

        visited = set()  # เก็บคำที่เคยเข้าคิวแล้ว จะได้ไม่วนลูปซ้ำ

        print(f"\n=== Start BFS ===")
        while queue:
            print(f"\nQueue: {list(queue)}")
            word, distance = queue.popleft()  # เอาคำและระยะทางออกมาจาก queue
            print(f"Dequeued: ({word}, {distance})")

            if word == endWord:
                print(f"Reached endWord: {word} at distance: {distance}")
                return distance  # ถ้าเจอ endWord แล้ว → ส่งระยะทางกลับ

            visited.add(word)  # mark ว่าคำนี้เคยไปแล้ว
            print(f"Visited: {visited}")

            # แปลงคำนี้เป็น pattern เพื่อลองหาคำที่เปลี่ยนได้ 1 ตัวอักษร
            for i in range(len(word)):
                tf = word[:i] + "*" + word[i + 1:]  # ทำ pattern เช่นเดิม
                print(f"  Pattern from '{word}': {tf}")

                potential_words = graph.get(tf, None)  # เอาคำทั้งหมดที่ match กับ pattern นี้

                if potential_words:
                    print(f"    Matches for {tf}: {potential_words}")
                    for potential_word in potential_words:
                        if potential_word not in visited:  # ถ้ายังไม่เคยไป
                            print(f"      -> Enqueue: {potential_word} (distance {distance + 1})")
                            queue.append((potential_word, distance + 1))  # เพิ่มเข้า queue พร้อมระยะทาง +1
                            visited.add(potential_word)  # mark visited ไปเลยตอนใส่ queue เพื่อกันใส่ซ้ำ
                else:
                    print(f"    No match for pattern: {tf}")

        print("End word not reachable.")
        return 0  # ถ้าหมดแล้วไม่เจอ endWord → แปลงไม่ได้

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]  # คำที่อนุญาตให้แปลงไปถึงได้

    sol = Solution()
    result = sol.ladderLength(beginWord, endWord, wordList)
    print(f"\nShortest transformation length from '{beginWord}' to '{endWord}': {result}")
