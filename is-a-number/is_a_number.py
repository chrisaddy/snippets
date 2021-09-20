import re
from typing import List

ONES = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19
}

TENS = {
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90
}

BLACKLIST = ["and"]

def tokenize(number: str) -> List[str]:
    tokens = re.split(r'\W+', number)
    return [token for token in tokens if token not in BLACKLIST]

def convert(number: str) -> int:
    pass
    

def check(number: str) -> bool:
    
    return False