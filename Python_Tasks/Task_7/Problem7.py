# Problem 7 - Alphabet Rangoli
https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alpha[size - 1:size - i - 1:-1]
        right = alpha[size - i - 1:size]
        row = "-".join(left + right)
        lines.append(row.center(4 * size - 3, "-"))

    print("\n".join(lines + lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
