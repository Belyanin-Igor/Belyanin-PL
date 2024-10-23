def count_words(sentence):
    words = sentence.rstrip('.').split()
    return len(words)
input_string = input("Введите строку, заканчивающуюся точкой: ")
if input_string.endswith('.'):
    word_count = count_words(input_string)
    print(f"Количество слов в строке: {word_count}")
else:
    print("Строка должна заканчиваться точкой.")