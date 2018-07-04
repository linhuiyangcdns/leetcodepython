"""

请编写一个函数，其功能是将输入的字符串反转过来。

示例：

输入：s = "hello"
返回："olleh"
"""
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        return s



if __name__ == "__main__":
    a = Solution()
    b = a.reverseString("hello")
    print(b)