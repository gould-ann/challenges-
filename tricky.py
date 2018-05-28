#https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
import math #lol

# arr = [1, 2, 3]
# mod_number = 2
# max([sum( [arr[j] if str(bin(i))[2:].zfill(len(arr))[j] == "1" else 0 for j in range(len(arr))] ) % mod_number for i in range(2**len(arr))])

def max_subarray(arr, mod_number):
    best_sum = 0
    for i in range(2**len(arr)):
        current_array = []
        bin_str = str(bin(i))[2:].zfill(len(arr))
        current_array = [arr[j] if bin_str[j] == "1" else 0 for j in range(len(arr))]
        best_sum = max(sum(current_array) % mod_number, best_sum)
    return best_sum

#this line
print max_subarray([3, 3, 9, 9, 5], 7)
