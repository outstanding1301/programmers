# https://programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭

import unittest
from functools import reduce

def solution(bridge_length, weight, truck_weights):
    Q = []
    remain = list(map(lambda x : [x, bridge_length], truck_weights))
    sec = 0
    while(len(remain) + len(Q) > 0):
        sec += 1
        Q = list(filter(lambda x : x[1] > 0, Q))
        weight_in_bridge = reduce(lambda x, y : x+y[0], Q, 0)
        if len(remain) > 0 and weight_in_bridge + remain[0][0] <= weight:
            Q.append(remain.pop(0))
        Q = list(map(lambda x : [x[0], x[1]-1], Q))
    return sec

class Solution(unittest.TestCase):
    def testSolution(self):
        self.assertEqual(solution(2, 10, [7,4,5,6]), 8)
        self.assertEqual(solution(100, 100, [10]), 101)
        self.assertEqual(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]), 110)