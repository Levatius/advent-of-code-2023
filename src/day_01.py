DIGIT_WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_digit(line, digit_words, search_func, evaluation_func):
    indexes = {word: search_func(line, word) for word in digit_words if word in line}
    word = evaluation_func(indexes, key=indexes.get)

    if word in DIGIT_WORDS:
        return DIGIT_WORDS[word]
    return word


def part_x(lines, digit_words):
    total = 0
    for line in lines:
        first_digit = find_digit(line, digit_words, search_func=str.find, evaluation_func=min)
        last_digit = find_digit(line, digit_words, search_func=str.rfind, evaluation_func=max)
        total += int(first_digit + last_digit)
    return total
