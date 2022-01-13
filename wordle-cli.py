# first we must load only 5 letter words to save RAM

word_list = []
with open('/usr/share/dict/words', 'r') as words_file:
    for line in words_file:
        word = line.rstrip()
        if len(word) == 5:
            word_list.append(word.lower())

print(word_list)