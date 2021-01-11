# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# print(two_sum([11, 2, 7, 15], 9))
# -> [1, 2]

# # this implementation has quadratic time complexity
# def twosum(arr, target):
#   for i in range(len(arr)):
#     for j in range(len(arr)):
#       if (i != j) and (arr[i] + arr[j] == target):
#         return [i, j]
# this implementation has linear time complexity
def twosum(arr, target):
  dictionary = {}
  for i in range(len(arr)):
    diff = str(target - arr[i])
    dictionary[diff] = i
  for j in range(len(arr)):
    value = str(arr[j])
    if dictionary.has_key(value) and j != dictionary[value]:
      return [j, dictionary[value]]
print(twoSum([11, 2, 7, 15], 9))
print(twosum([11, 5, 7, 3, 15], 10))