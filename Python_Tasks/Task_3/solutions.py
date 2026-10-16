# Task 3: Python Coding & Problem-Solving
# All 15 questions are implemented as reusable functions.

from collections import Counter


# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    """Return a dictionary containing each word and its frequency."""
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    """Return a dictionary containing each character and its frequency."""
    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1
    return counts


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_char(word):
    """Return the first character that occurs once, or None."""
    counts = Counter(word)
    for char in word:
        if counts[char] == 1:
            return char
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    """Return True when strings have the same characters and frequencies."""
    return Counter(s1) == Counter(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating_char(string):
    """Return the character whose second occurrence is encountered first."""
    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    """Return a new list with non-zero values first and zeros at the end."""
    non_zeros = [num for num in nums if num != 0]
    zeros = [num for num in nums if num == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest(nums):
    """Return the second-largest distinct value, or None if it does not exist."""
    unique_nums = sorted(set(nums), reverse=True)
    return unique_nums[1] if len(unique_nums) >= 2 else None


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
    """Return unique items in the order of their first appearance."""
    result = []
    seen = set()
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    """Return the missing value from the range 1 through n."""
    return n * (n + 1) // 2 - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first_pair(nums, target):
    """Return the earliest qualifying pair by second-element scan order."""
    seen = []
    for current in nums:
        needed = target - current
        for earlier in seen:
            if earlier == needed:
                return [earlier, current]
        seen.append(current)
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    """Return the value closest to zero; prefer positive on a tie."""
    if not nums:
        raise ValueError("nums must contain at least one number")
    return min(nums, key=lambda num: (abs(num), num < 0))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    """Return unique common values in their first-list order."""
    second_set = set(list2)
    result = []
    seen = set()
    for item in list1:
        if item in second_set and item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    """Return nums rotated right by k positions."""
    if not nums:
        return []
    k %= len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    """Return the largest sum of adjacent elements."""
    if len(nums) < 2:
        raise ValueError("nums must contain at least two elements")
    return max(nums[i] + nums[i + 1] for i in range(len(nums) - 1))


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_pairs_sum(nums, target):
    """Return unique ascending pairs, sorted by their first value."""
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(pair) for pair in sorted(pairs)]
