from curses.ascii import isdigit
import enum
from pathlib import Path

ROOT_DIR = Path(__name__).parent.resolve()

with open(ROOT_DIR / "day01" / "input.txt", 'r') as f:
    lines = f.read().splitlines()
    
string_to_int = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def string_to_int_func(string: str) -> int:
    n = len(string)
    first_dig = 0
    second_dig = 0
    
    word = ''
    done = False
    for i in range(n):
        if done:
            break
        
        if string[i].isdigit():
            first_dig = int(string[i])
            break
        
        for j in range(i, min(i + 5, n)):
            word += string[j]
            if word in string_to_int:
                first_dig = string_to_int[word]
                done = True
                break
            
        word = ''
    
    word = ''
    done = False
    
    for i in range(n - 1, -1, -1):
        if done:
            break
        
        c = string[i]
        if c.isdigit():
            second_dig = int(c)
            break
        
        condition = max(i - 5, -1)
        for j in range(i, max(i - 5, -1), -1):
            word += string[j]
            reversed_word = ''.join(reversed(word))
            if reversed_word in string_to_int:
                second_dig = string_to_int[reversed_word]
                done = True
                break
        
        word = ''
    
    return first_dig * 10 + second_dig

total = 0

for line in lines:
    val = string_to_int_func(line)
    print(f"{line} -> {val}")
    total += val
    
print(total)