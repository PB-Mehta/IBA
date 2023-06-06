from collections import Counter

def answer(str):
    words = str.split()
    word_count = Counter(words)
    highest_frequency_word = max(word_count, key=word_count.get)
    return len(highest_frequency_word)


input_str = input("Enter a string: ")
result = answer(input_str)
print(result)


 