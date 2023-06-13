import random
import time


def generate_initial_sequence_1(length):
    sequence = ""

    for _ in range(length):
        sequence += "()"

    return sequence

def generate_initial_sequence(length):
    opening_brackets = "([{</"
    closing_brackets = ")]}>\\"

    sequence = ""

    for _ in range(length):
        bracket_type = random.choice(opening_brackets)
        sequence += bracket_type

        closing_bracket = closing_brackets[opening_brackets.index(bracket_type)]
        sequence += closing_bracket

    return sequence

def isMatchingPair_1(opening, closing):
    if opening == '(' and closing == ')':
        return True
    return False

def isBalanced_1(expression):
    brackets = []

    for bracket in expression:
        if bracket == '(':
            brackets.append(bracket)
        elif bracket == ')':
            if len(brackets) == 0:
                return False
            top = brackets.pop()
            if not isMatchingPair_1(top, bracket):
                return False

    return len(brackets) == 0

def isMatchingPair_2(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '{' and closing == '}':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '<' and closing == '>':
        return True
    if opening == '/' and closing == '\\':
        return True
    return False

def isBalanced_2(expression):
    brackets = []

    for bracket in expression:
        if bracket in '({[</':
            brackets.append(bracket)
        elif bracket in ')}]>\\':
            if len(brackets) == 0:
                return False
            top = brackets.pop()
            if not isMatchingPair_2(top, bracket):
                return False

    return len(brackets) == 0


random.seed(time.time())
for length in range(500, 5001, 500):
    times = []
    bracketSequence = generate_initial_sequence_1(length)
    print(len(bracketSequence))
    print(isBalanced_1(bracketSequence))

    for i in range(12):
        start = time.perf_counter_ns()
        isBalanced_1(bracketSequence)
        end = time.perf_counter_ns()
        duration = end - start
        times.append(duration)

    print("length =", length)
    print()

    for time_val in times:
        print(time_val)