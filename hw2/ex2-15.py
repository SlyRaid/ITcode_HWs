# 15) 15) Выведите на экран следующую пирамидку:
# XX
# XxxX
# XxxxxX
# XxxxxxxX
# XxxxxxxxxX
# Ваша пирамидка должна соблюдать регистр как в примере.


for i in range(6):
    print('X' + 'x' * (2 * i) + 'X')
