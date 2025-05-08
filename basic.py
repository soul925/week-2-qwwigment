from collections import Counter

# 1. Check if Two Strings are Anagrams
def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# 2. Check if a Number is Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 3. Find the Most Frequent Element in a List
def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

# Example usage:
print("Anagram Test (listen, silent):", are_anagrams("listen", "silent"))  # True
print("Prime Test (29):", is_prime(29))  # True
print("Most Frequent ([1,2,3,2,2,4]):", most_frequent([1, 2, 3, 2, 2, 4]))  # 2
