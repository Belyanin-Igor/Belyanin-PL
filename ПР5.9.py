def count_word_occurrences(text, word):
    text = text.lower()
    word = word.lower()
    words = text.split()
    count = words.count(word)
    return count
if __name__ == "__main__":
    sample_text = "Это пример текста. Текст может содержать разные слова. Это текст для примера."
    search_word = "текст"
    occurrences = count_word_occurrences(sample_text, search_word)
    print(f"Слово '{search_word}' встречается {occurrences} раз(а) в тексте.")