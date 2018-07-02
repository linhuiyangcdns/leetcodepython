"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        i = 0
        while lenth > i :
            if nums[i] == 0:
                #nums.remove(nums[i])
                del nums[i]
                nums.append(0)
                lenth -= 1
                i -= 1

            i += 1
        return nums


if __name__ == "__main__":
    a = Solution()
    nums = a.moveZeroes([0,0,1])
    print(nums)