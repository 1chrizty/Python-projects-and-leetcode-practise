''' PALINDROME '''

# class Solution(object):
#     def isPalindrome(self, x):
#         if x < 0:
#             return False
        
#         original = x
#         reversed_num = 0
        
#         while x > 0:
#             digit = x % 10
#             reversed_num = (reversed_num * 10) + digit
#             x = x // 10
        
#         if original == reversed_num:
#             return True
#         else:
#             return False
# sol = Solution()
# print(sol.isPalindrome(121))
# print(sol.isPalindrome(-121))
# print(sol.isPalindrome(123))

'''Remove Duplicates from Sorted Array'''

# class Solution(object):
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0
#         k = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[k] = nums[i]
#                 k += 1
#         return k
# sol = Solution()
# nums = [1,1,1,2,3,4,4,5]
# k = sol.removeDuplicates(nums)
# print(f'Unique element count:{k}')
# print(f'Unique list:{nums[:k]}')
