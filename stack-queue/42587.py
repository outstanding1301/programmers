# https://programmers.co.kr/learn/courses/30/lessons/42587
# 프린터

import unittest

def solution(priorities, location):
    Q = list(map(lambda x: (x[1], x[0] == location), enumerate(priorities)))
    answer = 0
    while True:
        val = Q.pop(0)
        if len(Q) > 0 and val[0] < max(Q, key=lambda x: x[0])[0]:
            Q.append(val)
            continue
        answer += 1
        if val[1]:
            return answer

class Solution(unittest.TestCase):
    def testSolution(self):
        self.assertEqual(solution([1], 0), 1)
        self.assertEqual(solution([2, 1, 3, 2], 2), 1)
        self.assertEqual(solution([1, 1, 9, 1, 1, 1], 0), 5)