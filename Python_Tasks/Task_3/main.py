# Task 3: Import and test all 15 functions.
from solutions import (
    word_frequency, character_frequency, first_non_repeating_char,
    are_anagrams, first_repeating_char, move_zeros_to_end, second_highest,
    remove_duplicates, find_missing_number, two_sum_first_pair,
    closest_to_zero, common_elements, rotate_right, max_consecutive_sum,
    all_pairs_sum
)


def show(question, example, additional):
    print(f"\n{question}")
    print(f"  Given input -> {example[0]!r}")
    print(f"  Output      -> {example[1]!r}")
    print(f"  Extra test  -> {additional[0]!r}")
    print(f"  Extra output-> {additional[1]!r}")


if __name__ == "__main__":
    show("Q1. Word frequency",
         (("python is easy and python is powerful"),
          word_frequency("python is easy and python is powerful")),
         (("hello hello world"), word_frequency("hello hello world")))

    show("Q2. Character frequency",
         ("banana", character_frequency("banana")),
         ("letter", character_frequency("letter")))

    show("Q3. First non-repeating character",
         ("swiss", first_non_repeating_char("swiss")),
         ("aabbc", first_non_repeating_char("aabbc")))

    show("Q4. Anagrams",
         (("listen", "silent"), are_anagrams("listen", "silent")),
         (("hello", "world"), are_anagrams("hello", "world")))

    show("Q5. First repeating character",
         ("programming", first_repeating_char("programming")),
         ("abcdef", first_repeating_char("abcdef")))

    show("Q6. Move zeros to end",
         ([0, 3, 0, 1, 2, 0, 4], move_zeros_to_end([0, 3, 0, 1, 2, 0, 4])),
         ([0, 0, 5, 6], move_zeros_to_end([0, 0, 5, 6])))

    show("Q7. Second highest distinct number",
         ([10, 20, 40, 30, 40, 20], second_highest([10, 20, 40, 30, 40, 20])),
         ([7, 7, 7], second_highest([7, 7, 7])))

    show("Q8. Remove duplicates",
         ([4, 2, 4, 5, 2, 7, 5], remove_duplicates([4, 2, 4, 5, 2, 7, 5])),
         ([1, 1, 2, 3, 2], remove_duplicates([1, 1, 2, 3, 2])))

    show("Q9. Missing number",
         (([1, 2, 4, 5, 6], 6), find_missing_number([1, 2, 4, 5, 6], 6)),
         (([1, 3, 4], 4), find_missing_number([1, 3, 4], 4)))

    show("Q10. First pair for target",
         (([2, 7, 11, 15], 9), two_sum_first_pair([2, 7, 11, 15], 9)),
         (([1, 4, 2, 3], 5), two_sum_first_pair([1, 4, 2, 3], 5)))

    show("Q11. Closest to zero",
         ([-8, -3, 2, 5, -2], closest_to_zero([-8, -3, 2, 5, -2])),
         ([-4, -1, 1, 6], closest_to_zero([-4, -1, 1, 6])))

    show("Q12. Common elements",
         (([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]),
          common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])),
         (([3, 1, 3, 2], [2, 3]), common_elements([3, 1, 3, 2], [2, 3])))

    show("Q13. Rotate right",
         (([1, 2, 3, 4, 5], 2), rotate_right([1, 2, 3, 4, 5], 2)),
         (([1, 2, 3], 4), rotate_right([1, 2, 3], 4)))

    show("Q14. Maximum consecutive sum",
         ([4, 7, 2, 9, 5], max_consecutive_sum([4, 7, 2, 9, 5])),
         ([-5, -2, -8], max_consecutive_sum([-5, -2, -8])))

    show("Q15. All pairs for target",
         (([2, 4, 3, 5, 7, 8, 1], 9),
          all_pairs_sum([2, 4, 3, 5, 7, 8, 1], 9)),
         (([1, 2, 2, 3, 4], 5), all_pairs_sum([1, 2, 2, 3, 4], 5)))
