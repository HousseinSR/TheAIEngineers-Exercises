def count_words(text):
    # make text lowercase to be case-insensitive
    text = text.lower()
    
    # split text by spaces
    words = text.split()
    
    # use a dictionary to count occurrences
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count


# Example usage
text = "AI is the future. The future is now."
print(count_words(text))
