# 3) Расчет факториала числа с выводом каждого шага.

num = int(input())


def factorial(num):
    if num == 0 or num == 1:
        return 1
    x = factorial(num - 1) * num
    print(x)
    return x


factorial(num)

#------------------------------------

factorial = 1
for i in range(2, num + 1):
    print(factorial)
    factorial *= i

print(factorial)

#------------------------------------

factorial = 1
while num > 1:
    print(factorial)
    factorial *= num
    num -= 1

print(factorial)