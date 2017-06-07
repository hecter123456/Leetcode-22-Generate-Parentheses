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
        stack = [("",0,0)]
        for node,left,right in stack:
            flag = True
            if int(left) < n:
                stack.append((node+"(",int(left)+1,int(right)))
                flag = False
            if int(left) > int(right):
                stack.append((node+")",int(left),int(right)+1))
                flag = False
            if flag is True:
                Ans.append(node)
        return Ans

if __name__ == '__main__':
    unittest.main()
