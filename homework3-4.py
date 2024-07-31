

def single_root_words(root_word, *other_words):
    find_root = root_word.lower()
    same_word = []
    for i in other_words:
        a = i.lower()
        if find_root in a:
            same_word.append(i)
        if a in find_root:
            same_word.append(i)
    return same_word


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
