# 10) Вывести каждую букву строки в обратном порядке без использования reversed() или [::-1]


word = 'salam'

reverse_word = ''

for i in range(int(len(word)) - 1, -1, -1):
    reverse_word += word[i]

print(reverse_word)