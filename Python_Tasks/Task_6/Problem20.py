# Problem 20 -Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

def validate_phone_numbers():
    n = int(input())
    for _ in range(n):
        number = input().strip()
        # Regex explanation:
        # ^[789] -> starts with 7, 8, or 9
        # \d{9}$ -> followed by exactly 9 digits, ending the string
        if re.match(r"^[789]\d{9}$", number):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    validate_phone_numbers()
