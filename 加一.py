"""

给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = "".join(str(i)for i in digits)
        print(num)
        num2 = int(num) + 1
        list1 = list(str(num2))
        list2 = list(map(int,list1))
        return list2

if __name__ == "__main__":
    a = Solution()
    b = a.plusOne([4,3,2,1])
    print(b)