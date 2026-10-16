# Problem 19- Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        # Extract the substring of length k
        substring = string[i:i + k]
        
        # Remove duplicate characters while maintaining the original order
        unique_chars = "".join(dict.fromkeys(substring))
        
        # Print the result for this chunk
        print(unique_chars)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
