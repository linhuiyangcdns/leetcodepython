"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return None

        list_s = list(s)
        for i in range(len(s)):
            if list_s.count(s[i]) == 1:
                return i


if __name__ == "__main__":
    a = Solution()
    b = a.firstUniqChar("")
    print(b)
