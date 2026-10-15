first = input("first word: ")
second = input("second word: ")

def longerWord(first, second):
    if len(first) > len(second):
        return first
    if len(first) < len(second):
        return second
    elif len(first) == len(second):
        return first

print(longerWord(first, second))