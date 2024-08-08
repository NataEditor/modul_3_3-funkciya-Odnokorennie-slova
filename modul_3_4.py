dictionary = ['разговор', 'говорить', 'ГОВОР', 'беседовать', 'наМ', 'Вместе']
word = 'говор'

def single_root_word(root_word, *other_word):

    same_word = []
    for item in other_word:
        if item.lower() in root_word.lower() or root_word.lower() in item.lower():
            same_word.append(str(item).lower())
    print(*same_word)    

single_root_word(word, *dictionary)

