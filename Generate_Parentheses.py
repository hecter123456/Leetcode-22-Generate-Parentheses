import unittest

class unitest(unittest.TestCase):
    def testNumberZero(self):
        Ans = [""]
        n = 0
        self.assertEqual(Solution().generateParenthesis(n),Ans)
    def testNumberOne(self):
        Ans = ["()"]
        n = 1
        self.assertEqual(Solution().generateParenthesis(n),Ans)
    def testNumberTwo(self):
        Ans = ["(())","()()"]
        n = 2
        self.assertEqual(Solution().generateParenthesis(n),Ans)

class Solution(object):
    def generateParenthesis(self, n):
        Ans = []
        if n < 1:
            AnsStr = ""
            Ans.append(AnsStr)
            return Ans
        for i in range(0,n):
            AnsStr = "()"
            Ans.append(AnsStr)
        return Ans

if __name__ == '__main__':
    unittest.main()
