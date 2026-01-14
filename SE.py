# # Given an array of consecutive integers. Create a function that counts the sum of all elements
# inside the array within O(1) time.
# Sample array:
# arrayInteger = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output:
# 55
# Given an array of integers (sorted). Create a function that returns the index of a specific element
# within O(log(n)) time.
# Sample array:
# arrayInteger = [10, 23, 45, 92, 101, 102, 103, 10001]
# Input:
# 102
# Output:
# 5
# Given an array of integers (unsorted). Create a function that counts the number of occurrences
# of each element in the array.
# Sample array:
# arrayInteger = [5, 100, 12, 4, 5, 2, 12, 13]
# Output:
# 5 2x
# 100 1x
# 12 2x
# 4 1x
# 2 1x
# 13 1x


# NO 1
# def consecutiveArray(ARR):
#     n = len(ARR)
#     first = ARR[0]
#     last = ARR[n - 1]
#     print(n * (first + last) // 2)


# consecutiveArray([1,2,3,4,5,6,7,8,9,10])


# NO 2
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1


# arrayInteger = [10, 23, 45, 92, 101, 102, 103, 10001]
# print(binary_search(arrayInteger, 102))

# NO 3
def count_occurrences(arr):
    freq = {}

    for i in range(len(arr)):
        num = arr[i]
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1

    return freq


arrayInteger = [5, 100, 12, 4, 5, 2, 12, 13]
result = count_occurrences(arrayInteger)

for key in result:
    print(key, str(result[key]) + "x")



