# https://programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격

import unittest

def answer(idx, prices):
    res = 0
    for i in range(idx+1, len(prices)):
        res += 1
        if prices[idx] > prices[i]:
            return res
    return res

def solution(prices):
    res = prices
    for i in range(len(prices)):
        res[i] = answer(i, prices)
    return res

class Solution(unittest.TestCase):
    def testSolution(self):
        self.assertEqual(solution([1,2,3,2,3]), [4,3,1,1,0])