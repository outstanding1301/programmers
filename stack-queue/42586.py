# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기능개발

import unittest
import math

def solution(progresses, speeds):
    answer = [1]
    if len(progresses) == 1: return answer
    day = list(map(lambda x: math.ceil((100-x[0])/x[1]), zip(progresses, speeds)))
    stack = [day[0]]
    idx = 0
    for x in day[1:]:
        val = stack.pop()
        if x > val:
            idx += 1
            answer.append(0)
        answer[idx] += 1
        stack.append(max(val, x))
    return answer

class Solution(unittest.TestCase):
    def testSolution(self):
        self.assertEqual(solution([93, 30, 55], [1, 30, 5]), [2, 1])
        self.assertEqual(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]), [1, 3, 2])
        self.assertEqual(solution([1, 1, 1], [1, 1, 1]), [3])