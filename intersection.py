# def intersection(list1, list2):
#     result = []
#     for num1 in list1:
#         for num2 in list2:
#             if num1 == num2:
#                 result.append(num1)
#     return result

# def intersection(list1, list2):
#     dictionary = {}
#     result = []

#     for num1 in list1:
#         dictionary[str(num1)] = True

#     for num2 in list2:
#         if str(num2) in dictionary:
#             result.append(num2)

#     return result

# linear + linear = 2 * linear = linear O(n)

print(intersection([0, 1, 4, 5, 8], [0, 2, 7, 9, 4]))
#  -> [0, 4]

# def intersection(arr1, arr2):
#   arr3 = []
#   for i in arr1:
#     if i in arr2:
#       arr3.append(i)
#   return arr3

def intersection(arr1, arr2):
  # set([{'a': 1}, {'b': 2}])
  set1 = set(arr1)
  set2 = set(arr2)
  return list(set1 & set2)
print(intersection([0, 1, 4, 5, 8], [0, 2, 7, 9, 4]))