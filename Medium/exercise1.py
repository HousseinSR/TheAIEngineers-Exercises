def three_sum_target(nums, target):
    nums.sort()
    result = set()

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return [list(triplet) for triplet in result]


nums = [-1,0,1,2,-1,-4]
target = 0
print(three_sum_target(nums, target))
