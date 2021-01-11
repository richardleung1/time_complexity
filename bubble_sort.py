# while arr is not fully sorted:
  # first compare the two neighboring elements
  # i and i + 1
  # if they are backwards, swap them

# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(len(array) - 1):
#             if array[j] > array[j + 1]:
#                 num = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = num
#     return array

def is_sorted(arr):
  for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
      return False
  return True
def bubble_sort(arr):
  while not is_sorted(arr):
    print(arr)
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
  return arr
# print(is_sorted([1, 4, 6, 8, 9]))
# print(is_sorted([1, 4, 6, 3, 9]))
# print(bubble_sort([1, 4, 6, 3, 9]))
print(bubble_sort([9, 10, 1, -5, 4, 14, 20]))