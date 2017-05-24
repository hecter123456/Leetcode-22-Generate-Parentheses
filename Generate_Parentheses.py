import unittest

class unitest(unittest.TestCase):
    def testNumberEqualZero(self):
        Ans = [""]
        n = 0
        self.assertEqual(Solution().generateParenthesis(n),Ans)

class Solution(object):
    def generateParenthesis(self, n):
        Ans = []
        if n < 1:
            AnsStr = ""
            Ans.append(AnsStr)
            return Ans

if __name__ == '__main__':
    unittest.main()
