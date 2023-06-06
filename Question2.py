def is_valid_string(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the frequency of the most common character and the number of characters with that frequency
    max_freq = max(char_count.values())
    max_freq_count = sum(freq == max_freq for freq in char_count.values())

    # Check if the string is already valid or can be made valid by removing one character
    if max_freq_count == len(char_count) or (max_freq_count == len(char_count) - 1 and max_freq - 1 in char_count.values()):
        return "YES"
    else:
        return "NO"
