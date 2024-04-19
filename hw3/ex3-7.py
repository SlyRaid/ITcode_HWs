# 7) Проверить, является ли строка палиндромом (зеркальная)


slovo = input()

result = 'Строка является палиндромом'

for i in range(int(len(slovo) / 2)):
    if slovo[i] != slovo[-i - 1]:
        result = 'Строка не является палиндромом'
print(result)
