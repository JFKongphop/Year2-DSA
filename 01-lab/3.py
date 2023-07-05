nums = [10, 50, 9, 5, 120, 18]

length = len(nums)
min = nums[0]
max = nums[0]
for i in range(length):
  if nums[i] < min:
    min = nums[i]
  if (nums[i] > max):
    max = nums[i]
print(f"({min}, {max})")


def minmax(nums: list) -> tuple:
  data = sorted(nums)
  min = data[0]
  max = data[-1]
  return (min, max)

print(minmax(nums))

