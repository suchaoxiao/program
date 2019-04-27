'''  字符串的最大子序列
Given a string S and a string T, count the number of distinct subsequences of S which equals T.
A subsequence of a string is a new string which is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
    1.递归 ，把target拆分成一个一个个字符，看字符和字符串的匹配，然后循环调用字符比对函数实现递归
    2 dp
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        slen=len(s)
        tlen=len(t)
        if tlen>slen:
            return 0
        if tlen==slen:
            return 1 if t==s else 0
        if tlen==1:
            return s.count(t)
        tch=t[0]
        total_count=0
        for i ,ch in enumerate(s):
            if tch==ch:
                count=self.numDistinct(s[i+1:],t[1:])
                total_count+=count
        return total_count

    def numDistinct_dp(self,s,t):
        slen=len(s)
        tlen=len(t)
        dp=[[0]*(slen+1) for i in range(tlen+1)]
        for i in range(slen+1):
            dp[0][i]=1
        for i in range(1,tlen+1):
            tch=t[i-1]
            for j in range(i,slen+1):
                sch=s[j-1]
                if tch==sch:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]



def test():
    s=Solution()
    assert s.numDistinct_dp(s='rabbbit',t='rabbit')==3


