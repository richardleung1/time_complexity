# Under the hood, dictionaries involve hashing the key into a number, then treating that number as an address in an array
{'1': True, '0': True, '5': True, '4': True, '8': True}
'1' -> 239487
'0' -> 123
'5' -> 0977
ARRAY, 100 elements, start 987jhg76
|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
myArr[51] takes the same amount of time as myArr[1]
# O(n), linear time complexity
def linear_example(arr):
  for el in arr:
    print(el)
# O(1), constant time complexity
def constant_example(arr):
  print(arr[0])
  # OR
  print(len(arr))
# O(log(n)), logarithmic time complexity
def logarithmic_example(arr):
  while len(arr) > 1:
    arr = arr[1:len(arr) / 2]
  print('done!')
# alternate ending for log example
def other_log_example(number):
  guess = 1
  while guess < number:
    guess = guess * 2
  print('done!')
"good" constant complexity: O(1)
"bad" constant complexity: O(10) but we just write O(1)
green linear: medium slope; O(n)
blue linear: high slope; O(3n) but we just write O(n)
pink quadratic: steep curvature; O(n^2)
purple quadratic: shallow curvature; O(0.1n^2) but we just write O(n^2)
Combining time complexities:
          1 2 3
          4 5 6
          ______
          7 3 8
        6 1 5
      4 9 2
      __________
      5 6 0 8 8
The number of operations in the quadratic phase is swamps the number of operations in the linear phase as the input data size grows
So the time complexity might appear to be O(n^2 + n), but we simplify this to O(n^2) because the linear term's contribution is negligible for large values of n
# finding a specific value in an equally-spaced array is like opening a book to a specific page
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr[5]
constant time!
# finding a specific value in an unevenly spaced array requires binary search
# aka the split-in-half guessing game!
# which is logarithmic time
[0, 0.5, 1, 3.4, 4.7, 4.8, 4.9, 4.95, 5, 5.1, 5.2, 10]
example of binary search:
  target element is value of 5
  compare arr[5] to the value 5
  if arr[5] > 5
    go to small half (left half)
  else
    go to big half (right half)
# socks matching demo:
# each additional pair adds on n additional operations
# where n is the number of socks you already have
A B C D E F H G
H B D F G A C E
// this is a linear operation in disguise!
// under the hood, indexOf (as well as `el in arr`) uses a brute force find, aka a for-loop
someArray.indexOf(4)