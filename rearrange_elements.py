def sample(nums):
	left, mid, right = 0, 0, len(nums) -1
	while mid <= right:
		if nums [mid] == 0:
			temp = nums [left]
			nums[left] = nums [mid]
			nums [mid] = temp
			left += 1
			mid += 1 
		elif(nums [mid] == 1):
			mid += 1
		else:
			temp = nums [mid]
			nums [mid] = nums [right]
			nums [right] = temp
			right -= 1
		print(mid, right)
		return nums
nums = [0, 2, 1, 1, 2, 0, 1, 1, 2, 0]
print(sample(nums))