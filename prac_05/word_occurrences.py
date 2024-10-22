"""
CP1404/CP5632 Practical
"""
def count_word_occurrences():
    text = input("Text: ")

    text = text.lower()

    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word_count = dict(sorted(word_count.items()))

    max_word_length = max(len(word) for word in sorted_word_count)

    for word, count in sorted_word_count.items():
        print(f"{word:{max_word_length}} : {count}")

if __name__ == "__main__":
    count_word_occurrences()

