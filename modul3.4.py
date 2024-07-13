def single_root_words(root_word, *other_words):
    same_word = []
    root_word_lower = root_word.lower()
    for j in other_words:
        other_words_lower = j.lower()
        if (other_words_lower in root_word_lower) or (root_word_lower in other_words_lower):
            same_word.append(other_words_lower)
    return same_word

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

#['richiest', 'orichalcum', 'richies']
#['Able', 'Disable']