# 8) Определить, содержит ли список дубликаты


words = ['яхта', 'пока', 'привет', 'корень', 'яхта', 'дерево', 'привет', 'правда', 'кайф']
new_words = []
second_word = []

test_set = set(words)
print(len(words) != len(test_set))

for i in words:
    if i in new_words:
        second_word.append(i)
    else:
        new_words.append(i)

if len(second_word) > 0:
    print(True)
else:
    print(False)