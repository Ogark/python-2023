def make_oneline(string):
    return string.replace('\n ', ' ').replace('\n', ' ').strip()
def average_word_length(txt):
    words = txt.split()  # Розділити текст на слова за допомогою пробілів
    word_lengths = [len(word) for word in words]  # Створити список довжин слів
    if word_lengths:  # Перевірити, чи є слова у тексті
        return sum(word_lengths) / len(word_lengths)  # Обчислити середню довжину слів
    else:
        return 0  # Повернути 0, якщо немає слів
def total_characters_and_word_count(txt):
    # Обчислити загальну довжину символів у тексті
    total_characters = len(txt)

    # Розділити текст на слова за допомогою пробілів
    words = txt.split()

    # Обчислити кількість слів у тексті
    word_count = len(words)

    return total_characters, word_count
from collections import Counter
def most_common_words(txt, n=10):
    words = txt.split()
    word_count = Counter(words)
    common_words = word_count.most_common(n)
    return common_words


demo = """
Aeneas was a robust guy,
A kozak full of vim,
Full of the devil, lewd and spry,
There was no one like him.
And when the Greeks had burned down Troy
And made of it, to their great joy,
A heap of dung, he left that waste
Together with some Trojan tramps,
The sun-tanned scamps.
They all took to their heels in haste.
"""
#demo = make_oneline(demo)

# Обчислити середню довжину слів у тексті
average_len = average_word_length(demo)
print(f"Average word length in text: {average_len:.2f} characters")

# Виклик нової функції для обчислення загальної довжини символів і кількості слів
total_chars, word_count = total_characters_and_word_count(demo)
print(f"Total length of characters in the text: {total_chars} characters")
print(f"Number of words in the text: {word_count} words")

# Приклад використання для знаходження 10 найчастіше вживаних слів
common_words = most_common_words(demo, n=10)
print("10 most frequently used words:")
for word, count in common_words:
    print(f"{word}: {count} times")

def symbols_count(txt):
    """Build mapping counting number of entries of each symbol.

    ...
    """
    syms = set(txt)
    res = dict()
    for sym in sorted(syms):
        res[sym] = txt.count(sym)
    return res
    # or
    # return {sym: txt.count(sym) for sym in sorted(set(txt))}


class Text:
    def __init__(self, obj=''):
        self.str = str(obj)
        self.oneline = make_oneline(self.str)

    def __repr__(self):
        lim = self.oneline[:16]
        ext = '...' if len(self.oneline) > 16 else ''
        return f'{type(self).__name__}({repr(lim)}{ext})'

    def __str__(self):
        return self.str

    def symbols_count(self):
        """... same as above ..."""
        return {sym: self.oneline.count(sym)
                for sym in sorted(set(self.oneline))}


