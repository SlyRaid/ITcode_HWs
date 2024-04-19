# 6) Подсчитать количество цифр в числе. Реализовать двумя видами циклов


numbers = 123456789

count = 0
for i in list(str(numbers)):
    count += 1

print(count)

count2 = 0
while numbers > 0:
    numbers //= 10
    count2 += 1

print(count2)