def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index in range(0, len(nums) - 1):
        for index_to_sum in range(index + 1, len(nums)):
            sum = nums[index] + nums[index_to_sum]
            if sum == target:
                return [index, index_to_sum]

solution = twoSum([3,2,4], 6)
print(solution)
