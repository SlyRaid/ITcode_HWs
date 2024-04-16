students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

# 1. Все люди
all_people = students.union(employees)
print(all_people)

# 2. Люди, которые одновременно учатся и работают:
both = students.intersection(employees)
print(both)

# 3. Люди, которые только работают, но не учатся:
only_employees = employees.difference(students)
print(only_employees)

# 4. Люди, которые либо учатся, либо работают, но не одновременно:
either_or = students.symmetric_difference(employees)
print(either_or)
