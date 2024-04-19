# 9) Удалить все дубликаты из списка без использования дополнительных структур. Реализовать двумя видами циклов,
# для удаления можно использовать pop() либо del


words = ['яхта', 'пока', 'привет', 'корень', 'яхта', 'дерево', 'привет', 'правда', 'кайф', 'корень']


new_words = []
print(words)
for i, j in enumerate(words):
    if j in new_words:
        words.pop(i)
    else:
        new_words.append(j)
print(words)




print(words)

i = 0
while i < len(words):
    j = i + 1
    while j < len(words):
        if words[i] == words[j]:
            del words[j]
        else:
            j += 1
    i += 1


print(words)