# Join first and last digits of each line and sum the lines. Digits may be written extensively.

import sys
import re

numdict = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

def match_first(match_dict, text):
    for i in range(len(text)):
            if str.isdigit(text[i]):
                return text[i]
            for word, value in match_dict.items():
                if re.match("^"+word, text[i:]):
                    return value

total = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        firstnum = match_first(numdict, line)
        reverse_numdict = {word[::-1]:value for word,value in numdict.items()}
        lastnum = match_first(reverse_numdict, line[::-1])
        total += int(firstnum+lastnum)

print(total)
