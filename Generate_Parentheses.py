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
    def generateParenthesis(self, n):
        Ans = []
        stack = [("",int(0),int(0))]
        for node,left,right in stack:
            if left < n:
                stack.append((node+"(",left+1,right))
            if left > right:
                stack.append((node+")",left,right+1))
            if right ==  n:
                Ans.append(node)
        return Ans

if __name__ == '__main__':
    unittest.main()
