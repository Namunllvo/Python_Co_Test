class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            i_val = nums[i]
            for j in range(1, len(nums)):
                j_val = nums[j]
                if i == j: # 같은걸 뽑아서 제출한 경우 제외 - 탈출
                    break
                if i_val + j_val == target:
                    result.append(i)
                    result.append(j)
                    return result