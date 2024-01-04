#https://www.codewars.com/kata/51e056fe544cf36c410000fb

from collections import Counter
import re

def top_3_words(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    words = [word for word in words if word != "'" and not word.startswith("''")]
    word_counts = Counter(words)
    top_words = [word for word, _ in word_counts.most_common(3)]

    return top_words