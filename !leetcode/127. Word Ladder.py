from typing import List  # สำหรับประกาศ type hint เช่น List[str]
# defaultdict ช่วยให้สร้าง dict ที่มีค่า default ได้ / deque ใช้เป็น queue
# แบบมีประสิทธิภาพสูง
from collections import defaultdict, deque

# array[start:end:step] เป็น syntax slicing ทั่วไป เช่น [1:5] เอาตำแหน่ง 1
# ถึง 4


class Solution:
    def ladderLength(
            self,
            beginWord: str,
            endWord: str,
            wordList: List[str]) -> int:
        # เงื่อนไขพิเศษ: ถ้า begin == end และ end ไม่อยู่ใน wordList →
        # ไม่มีทางแปลงได้
        if beginWord == endWord and endWord not in wordList:
            return 0

        # graph จะเก็บ key = pattern เช่น "h*t", "*ot", "ho*" → value = คำที่
        # match กับ pattern นั้น
        graph = defaultdict(list)

        # สร้าง pattern ของทุกคำใน wordList
        for word in wordList:
            for i in range(len(word)):
                # แปลงตำแหน่งที่ i ให้เป็น "*" เช่น "hot" → "*ot", "h*t", "ho*"
                tf = word[:i] + "*" + word[i + 1:]
                graph[tf].append(word)  # เพิ่มคำเข้า list ของ pattern นั้น

        print(graph)  # debug: แสดง graph ที่สร้างขึ้น

        # เริ่ม BFS โดยใช้ queue เก็บ (word, current_distance)
        # ระยะเริ่มต้น = 1 (เพราะเริ่มจาก beginWord แล้วนับคำด้วย)
        queue = deque([(beginWord, 1)])

        visited = set()  # เก็บคำที่เคยเข้าคิวแล้ว จะได้ไม่วนลูปซ้ำ

        while queue:
            word, distance = queue.popleft()  # เอาคำและระยะทางออกมาจาก queue

            if word == endWord:
                return distance  # ถ้าเจอ endWord แล้ว → ส่งระยะทางกลับ

            visited.add(word)  # mark ว่าคำนี้เคยไปแล้ว

            # แปลงคำนี้เป็น pattern เพื่อลองหาคำที่เปลี่ยนได้ 1 ตัวอักษร
            for i in range(len(word)):
                tf = word[:i] + "*" + word[i + 1:]  # ทำ pattern เช่นเดิม

                # เอาคำทั้งหมดที่ match กับ pattern นี้
                potential_words = graph.get(tf, None)

                if potential_words:
                    for potential_word in potential_words:
                        if potential_word not in visited:  # ถ้ายังไม่เคยไป
                            # เพิ่มเข้า queue พร้อมระยะทาง +1
                            queue.append((potential_word, distance + 1))
                            # mark visited ไปเลยตอนใส่ queue เพื่อกันใส่ซ้ำ
                            visited.add(potential_word)

        return 0  # ถ้าหมดแล้วไม่เจอ endWord → แปลงไม่ได้


# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    # คำที่อนุญาตให้แปลงไปถึงได้
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    sol = Solution()
    # ควร print 5 → hit → hot → dot → dog → cog
    print(sol.ladderLength(beginWord, endWord, wordList))
