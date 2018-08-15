"""
58. 最后一个单词的长度
题目描述提示帮助提交记录社区讨论阅读解答
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5

思路：空格切片，取最后字符串长度
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        alist = s.split()
        if len(alist) == 0:
            return 0
        return len(alist[-1])
