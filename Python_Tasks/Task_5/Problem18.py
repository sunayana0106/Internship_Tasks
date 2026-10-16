# Problem 18- The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    
    stuart_score = 0
    kevin_score = 0
    string_length = len(string)
    
    for i in range(string_length):
        if string[i] in vowels:
            kevin_score += string_length - i
        else:
            stuart_score += string_length - i
            
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
