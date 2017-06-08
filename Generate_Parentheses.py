import unittest

class unitest(unittest.TestCase):
    def testNumberEqualZero(self):
        Ans = [""]
        n = 0
        self.assertEqual(Solution().generateParenthesis(n),Ans)
    def testNumberEqualOne(self):
        Ans = ["()"]
        n = 1
        self.assertEqual(Solution().generateParenthesis(n),Ans)
    def testNumberEqualTwo(self):
        Ans = ["(())","()()"]
        n = 2
        self.assertEqual(Solution().generateParenthesis(n),Ans)

class Solution(object):
    def generateParenthesis(self, n, diff = 0):
        if n > 0 <= diff:
            return ["(" + q for q in self.generateParenthesis(n-1, diff+1)] + \
                   [")" + q for q in self.generateParenthesis(n, diff-1)]
        return [')' * diff] * (not n)
        

if __name__ == '__main__':
    unittest.main()
